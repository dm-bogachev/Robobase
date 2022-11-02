function tablesFilter() {
    var trs = document.querySelectorAll('#filteredTable tr:not(.header)')
    var filter = document.querySelector('#filterInput').value
    var filter_split = filter.split(';')
    for (let i = 0; i < filter_split.length; i++) {
        const regex = new RegExp(filter_split[i], 'i')
        const isFoundInTds = td => regex.test(td.innerHTML)
        const isFound = childrenArr => childrenArr.some(isFoundInTds)
        const setTrStyleDisplay = ({ style, classList, children }) => {
            style.display = isFound([
                ...children // <-- All columns
            ]) ? '' : 'none'
            classList.add(isFound([
                ...children // <-- All columns
            ]) ? 'keep' : 'filter')
            classList.remove(!isFound([
                ...children // <-- All columns
            ]) ? 'keep' : 'filter')
        }
        trs.forEach(setTrStyleDisplay)
        trs = document.querySelectorAll('.keep')
    }
}