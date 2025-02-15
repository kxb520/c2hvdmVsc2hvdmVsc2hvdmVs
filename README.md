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
    <a href="#-贡献指南">🤝 参与贡献</a>
  </p>

[![Made with React Router](https://img.shields.io/badge/Made%20with-React%20Router-FF4B2B?style=for-the-badge&logo=react-router&logoColor=white)](https://reactrouter.com/)
[![Made with Ant Design](https://img.shields.io/badge/Made%20with-Ant%20Design-0170FE?style=for-the-badge&logo=ant-design&logoColor=white)](https://ant.design/)
[![Made with MapLibre GL JS](https://img.shields.io/badge/Made%20with-MapLibre%20GL%20JS-1A73E8?style=for-the-badge&logo=mapbox&logoColor=white)](https://maplibre.org/)
[![Made with Hammer.js](https://img.shields.io/badge/Made%20with-Hammer.js-FCA121?style=for-the-badge&logo=javascript&logoColor=black)](https://hammerjs.github.io/)
[![Powered by Nginx](https://img.shields.io/badge/Powered%20by-Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/)


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

**Shovel** 是一款面向现代企业安全团队的开源资产测绘平台。通过融合主被动扫描引擎、多模态数据关联分析和智能风险评估模型，我们致力于为企业提供更优雅的资产治理解决方案。

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


### 🌟 为什么选择Shovel？
- 更全面： 自动发现多平台资产，超多规则构建清晰资产图谱，告别盲区。
- 更高效： 创新资产组管理，简化流程，解放生产力。
- 更自由： 开放 API & 插件，灵活集成各类安全工具，定制专属方案，摆脱厂商绑定。
- 更快速： 高性能插件系统，快速定制工作流，加速创新落地。
- 更灵活： 分离式架构，支持多种部署模式，适应各种企业规模。


### ⚡ 快速部署

```
待完善
```




### 🧩 插件生态系统

#### 官方插件集（持续更新）

| 插件名称                | 功能描述                                                                 | 标签                                                                 |
|-------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------|
| **Fingerprinter**       | 根据任务中的URL信息进行CMS指纹识别                                       | `info-collecting`, `collector`, `discovery`, `identification`, `CMS` |
| **Nmapper**             | 根据任务中的Host信息，使用Nmap扫描器进行端口探测并识别服务               | `info-collecting`, `collector`, `network`, `nmap`, `port`, `discovery`, `CIDR` |
| **Fofa_Mapper**         | 根据任务中的域名信息，使用FOFA进行信息收集                               | `info-collecting`, `collector`, `domain`, `FOFA`                     |
| **Http_Port_Visitor**   | 根据任务中的开放端口信息，进行相关Web服务的信息收集                      | `httpx`, `info-collecting`, `collector`, `ports`, `http`             |
| **Company_Investigator**| 根据任务中的公司/集团名进行ICP备案信息收集                               | `info-collecting`, `collector`, `company`, `enscan`, `unstable`      |
| **Domain_Seeker**       | 根据任务中的域名信息，进行子域名信息收集                                 | `info-collecting`, `collector`, `website`, `discovery`, `domain`, `DNS`, `amass` |
| **Nuclei_Reactor**      | 根据任务中的URL信息，使用Nuclei扫描器进行漏洞检测                        | `vulnerability`, `detection`, `nuclei`, `exploit`, `CVE`             |

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

让我们一起打造更强大的Shovel插件生态！🚀
