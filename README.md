<div align="center">
  <a href="https://www.hscsec.cn">
    <img src="./img/favicon.ico" alt="shovel" height="80" />
  </a>
  <h1>
    <b>SHOVEL</b>
  </h1>
  

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=ZCOOL+KuaiLe&pause=1000&color=F7F7F7&center=true&vCenter=true&width=435&lines=%E8%A7%A3%E6%94%BE%E5%8F%8C%E6%89%8B%EF%BC%8C%E4%B8%8D%E5%81%9A%E5%90%97%E5%96%BD" alt="Typing SVG" /></a>

<p align="center">
    <a href="#-重新定义企业资产管理范式">🔍 概述</a> •
    <a href="#-核心优势">🚀 核心优势</a> •
    <a href="#-快速部署">⚡ 快速部署</a> •
    <a href="#-插件生态系统">🧩 插件生态</a> •
    <a href="#-欢迎贡献插件">🤝 参与贡献</a>
  </p>

[![Built with React Router](https://img.shields.io/badge/Built_with-React_Router-FF4154?style=for-the-badge&logo=react-router&logoColor=white)](https://reactrouter.com/)
[![Designed with Ant Design](https://img.shields.io/badge/Designed_with-Ant_Design-1890FF?style=for-the-badge&logo=ant-design&logoColor=white)](https://ant.design/)
[![Mapped with MapLibre GL JS](https://img.shields.io/badge/Mapped_with-MapLibre_GL_JS-4264FB?style=for-the-badge&logo=mapbox&logoColor=white)](https://maplibre.org/)
[![Powered by Hammer.js](https://img.shields.io/badge/Powered_by-Hammer.js-FFCA28?style=for-the-badge&logo=javascript&logoColor=black)](https://hammerjs.github.io/)
[![Served by Nginx](https://img.shields.io/badge/Served_by-Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/)

  <p>
    <sub>
      Powered with ❤️ by
      <a href="https://www.hscsec.cn">
        <b>HSC Security</b>
      </a>
    </sub>
  </p>
</div>

<img src="./img/shovel.jpg?raw=true" alt="shovel" style="width: 100%;">

</div>




### 🔍 重新定义企业资产管理范式

**Shovel** 是一款面向现代企业安全团队的开源资产测绘平台。通过融合主被动扫描引擎、多模态数据关联分析和智能风险评估模型，我们致力于解放安全行业重复劳动者的双手、为企业提供更优雅的资产治理解决方案。

------

### 🚀 核心优势

- **构建全面的资产视图：**
  自动发现并关联多平台资产，利用包含超多规则，为您呈现清晰的空间资产图谱，让您对资产状况一目了然。
- **革新资产管理方式：**
  通过创新的资产组概念，简化企业任务和资产的管理流程，提高效率。
- **自由集成，无限可能：**
  提供标准化 OpenAPI 和插件 API，赋能开发者和社区，灵活集成各类安全工具与平台，打造定制化的安全解决方案。
- **快速定制工作流：**
  高性能管道式插件系统，让您可以灵活定制和扩展执行逻辑，快速将想法转化为实际应用。
- **适应各种部署环境：**
  核心与中间层分离的架构，支持分布式、链式和边缘设备等多种部署模式，满足您多样化的需求。


### ✨ 为什么选择shovel

| 特性维度     | 传统方案         | SHOVEL 解决方案        | 核心优势体现                             |
| ------------ | ---------------- | ---------------------- | ---------------------------------------- |
| **资产发现** | ❌ 被动式人工录入 | ✅ 主动+被动自动化发现  | 更全面：多平台资产自动发现，资产面覆盖完全 |
| **分析资产** | ❌ 缺乏系统管理，只关注单次任务   | ✅ 资产自动指纹分类，系统性管理资产组     | 更高效：自动构建资产关系网络             |
| **风险检测** | ❌ POC指纹更新缓慢   | ✅ 超多POC指纹库实时更新 | 更强大：及时跟进，铲除隐患                 |
| **扩展能力** | ❌ 封闭式系统     | ✅ 开放式插件架构       | 更自由：API+插件灵活扩展                 |
| **架构设计** | ❌ 单体架构       | ✅ 核心与中间件分离架构 | 更灵活：支持分布式/边缘部署              |


### ⚡ 快速部署

#### 一键部署
```
待完善
```

#### 镜像部署
```
待完善
```



### 🧩 插件生态系统

#### 官方基础插件集（持续更新）


| 插件名称                | 功能描述                                                                 | 标签                                                                 |
|-------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------|
| **fingerprinter**       | 根据任务中的URL信息进行CMS指纹识别                                       | `info-collecting`, `collector`, `discovery`, `identification`, `CMS` |
| **nmapper**             | 根据任务中的Host信息，使用Nmap扫描器进行端口探测并识别服务               | `info-collecting`, `collector`, `network`, `nmap`, `port`, `discovery`, `CIDR` |
| **fofa_mapper**         | 根据任务中的域名信息，使用FOFA进行信息收集                               | `info-collecting`, `collector`, `domain`, `FOFA`                     |
| **http_port_visitor**   | 根据任务中的开放端口信息，进行相关Web服务的信息收集                      | `httpx`, `info-collecting`, `collector`, `ports`, `http`             |
| **company_Investigator**| 根据任务中的公司/集团名进行ICP备案信息收集                               | `info-collecting`, `collector`, `company`, `enscan`, `unstable`      |
| **domain_Seeker**       | 根据任务中的域名信息，进行子域名信息收集                                 | `info-collecting`, `collector`, `website`, `discovery`, `domain`, `DNS`, `amass` |
| **nuclei_Reactor**      | 根据任务中的URL信息，使用Nuclei扫描器进行漏洞检测                        | `vulnerability`, `detection`, `nuclei`, `exploit`, `CVE`             |

* 插件仓库: 待完善

---

### 🛠️ 插件开发指南（即将发布）

我们正在编写详细的插件开发文档，包括：
- **插件开发框架详解**：从零开始构建一个插件
- **核心API参考手册**：了解Shovel提供的核心接口
- **插件调试与测试**：如何高效调试和验证插件功能
- **插件发布流程**：将你的插件贡献到官方或社区插件库

---

### 🌱 欢迎贡献插件

我们鼓励开发者参与插件生态建设：
1. **提交插件**：将你的插件代码提交到我们的[插件仓库](https://github.com/your-repo/shovel-plugins)
2. **插件审核**：经过审核后，优质插件将被纳入官方插件库
3. **社区奖励**：贡献者将获得专属荣誉标识和社区积分

---

### 📢 温馨提示

- **插件编写指南**：详细的插件开发Wiki将在近期发布，敬请期待！
- **插件反馈**：如果你对现有插件有任何建议或发现问题，欢迎提交[Issue](https://github.com/your-repo/shovel/issues)
- **插件需求**：如果你有新的插件需求，欢迎在[讨论区](https://github.com/your-repo/shovel/discussions)提出

---

## 🎉 鸣谢

- https://github.com/owasp-amass/amass
- https://github.com/wgpsec/ENScan_GO
- https://github.com/projectdiscovery/nuclei
- https://github.com/antvis/L7

---
📌 法律声明：本工具仅限合法授权测试使用，开发者不对滥用行为负责<br> 
📧 商务合作：shovel@hscsec.cn | 🌐 官网：https://www.hscsec.cn


让我们一起打造更强大的Shovel插件生态！🚀
