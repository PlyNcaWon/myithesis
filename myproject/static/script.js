// ฟังก์ชันอัปโหลดเอกสารวิทยานิพนธ์
uploadThesisForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData(event.target);

  fetch('/upload-thesis/', {
    method: 'POST',
    body: formData,
  })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        alert(data.error);
      } else {
        alert(data.success);
        downloadThesisList(); // รีเฟรชรายการเอกสารวิทยานิพนธ์
      }
    })
    .catch(error => {
      alert('เกิดข้อผิดพลาด: ' + error.message);
    });
});

// ฟังก์ชันแปลงไฟล์ Word เป็น PDF
convertThesisForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData(event.target);

  fetch('/convert-thesis/', {
    method: 'POST',
    body: formData,
  })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        alert(data.error);
      } else {
        alert(data.success);
        downloadThesisList(); // รีเฟรชรายการเอกสารวิทยานิพนธ์
      }
    })
    .catch(error => {
      alert('เกิดข้อผิดพลาด: ' + error.message);
    });
});

// ฟังก์ชันตรวจสอบรูปแบบเอกสาร
checkFormatForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData(event.target);

  fetch('/check-format/', {
    method: 'POST',
    body: formData,
  })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        alert(data.error);
      } else {
        alert('รูปแบบเอกสารคือ: ' + data.format);
      }
    })
    .catch(error => {
      alert('เกิดข้อผิดพลาด: ' + error.message);
    });
});

// ฟังก์ชันดาวน์โหลดเอกสารวิทยานิพนธ์
function downloadThesisList() {
  fetch('/download-thesis/')
    .then(response => response.json())
    .then(data => {
      downloadThesisList.innerHTML = '';

      data.forEach(thesis => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
          <a href="<span class="math-inline">\{thesis\.url\}" download\="</span>{thesis.filename}">${thesis.filename}</a>
        `;
        downloadThesisList.appendChild(listItem);
      });
    })
    .catch(error => {
      alert('เกิดข้อผิดพลาด: ' + error.message);
    });
}

// ฟังก์ชันลบเอกสารวิทยานิพนธ์
deleteThesisForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const thesisId = document.getElementById('thesis_id').value;

  fetch(`/delete-thesis/${thesisId}/`, {
    method: 'POST',
  })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        alert(data.error);
      } else {
        alert(data.success);
        downloadThesisList(); // รีเฟรชรายการเอกสารวิทยานิพนธ์
      }
    })
    .catch(error => {
      alert('เกิดข้อผิดพลาด: ' + error.message);
    });
});

// ฟังก์ชันค้นหาเอกสารวิทยานิพนธ์
searchThesisForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const searchTerm = document.getElementById('search_term').value;

  fetch(`/search-thesis/?q=${searchTerm}`)
    .then(response => response.json())
    .then(data => {
      downloadThesisList.innerHTML = '';

      data.forEach(thesis => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
          <a href="${thesis.url}" download="${thesis.filename}">${thesis.filename}</a>
        `;
        downloadThesisList.appendChild(listItem);
      });
    })
    .catch(error => {
      alert('เกิดข้อผิดพลาด: ' + error.message);
    });
});
