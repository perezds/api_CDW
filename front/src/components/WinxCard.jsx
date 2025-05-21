import './WinxCard.css';

function WinxCard({ name, image, destaque }) {
    return (
      <div className={`winx-card ${destaque ? 'destaque' : ''}`}>
        <img className="winx-card-image" src={image} alt={name} />
        <h3 className="winx-card-title">{name}</h3>
      </div>
    );
  }
  
export default WinxCard;
