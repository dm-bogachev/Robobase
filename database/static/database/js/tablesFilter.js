function tablesFilter() {
    const trs = document.querySelectorAll('#filteredTable tr:not(.header)')
    const filter = document.querySelector('#filterInput').value
    const regex = new RegExp(filter, 'i')
    const isFoundInTds = td => regex.test(td.innerHTML)
    const isFound = childrenArr => childrenArr.some(isFoundInTds)
    const setTrStyleDisplay = ({ style, children }) => {
        style.display = isFound([
            ...children // <-- All columns
        ]) ? '' : 'none'
    }
    trs.forEach(setTrStyleDisplay)
}