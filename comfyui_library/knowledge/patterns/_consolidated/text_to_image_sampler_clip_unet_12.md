---
name: text_to_image_sampler_clip_unet_12
type: Text To Image
frequency: 24
level: weak
coverage: 0.919875
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/【开箱即用】KREA-2-FP8_文生图基础流_新任生图王者_风格万变_2069375033096622081.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_V2版_2105216145447014402.json, 图片生成/文生图/【老金驿站】Anima二次元专属出图工作流_2019258717857914882.json, 图片生成/文生图/【通义-ZImage文生图】最强小参数大猛兽！ 极致速度、极致质量、极致性价比。_1994129975662100482.json, 图片生成/文生图/【遇见AI】Krea2 Lip BIting 咬嘴唇lora_2082379890434854914.json, 图片生成/文生图/【遇见AI】Krea2文生图基础工作流_2069621635891679234.json, 图片生成/文生图/【遇见AI】Z-image turbo基础文生图_2053775081775611905.json, 图片生成/文生图/【遇见AI】Z-image 基础文生图_2053780457782816769.json, 图片生成/文生图/【遇见AI】boogu image base基础工作流_2067907838378340354.json, 图片生成/文生图/【遇见AI】boogu image turbo 基础工作流_2067908137574813697.json, 图片生成/文生图/【遇见AI】flex2-preview 基础文生图_2049429860640100354.json, 图片生成/文生图/千问qwen-image-2.1文生图_2108106051034894338.json, 图片生成/文生图/千问qwen-image-2.1文生图_2112373946829066242.json, 图片生成/文生图/千问qwen-image-2.1文生图_2113920786338770946.json, 图片生成/文生图/千问qwen-image-2.1文生图｜人像写真美少女风格随心出_2114280952854831105.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜_2107739693239590914.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜_2110564054040403969.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜_2111007985395916802.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜注意仅供学习不可商用_2104770730121588737.json, 图片生成/文生图/图图工作流人像写真｜Krea2文生图摄影出图_2095578272632496130.json, 图片生成/文生图/图图组合文生图玩法｜Krea2 多图融合一键出图_2096264881749184513.json, 图片生成/文生图/图生图任意角度转换双图版｜Qwen Image2.1 多角度出图更立体_2105540395974348802.json, 图片生成/文生图/文生图ZImage工作流｜多段提示词同时出图神器_2100813214991863810.json, 视频生成/文生视频/AI角色姿态导演台Character Pose Director，文生视频图生视频姿势精准控制_2103202510185000962.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/文生图/【开箱即用】KREA-2-FP8_文生图基础流_新任生图王者_风格万变_2069375033096622081.json、图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_V2版_2105216145447014402.json、图片生成/文生图/【老金驿站】Anima二次元专属出图工作流_2019258717857914882.json、图片生成/文生图/【通义-ZImage文生图】最强小参数大猛兽！ 极致速度、极致质量、极致性价比。_1994129975662100482.json、图片生成/文生图/【遇见AI】Krea2 Lip BIting 咬嘴唇lora_2082379890434854914.json…）

- **类型**：Text To Image
- **样本数**：24
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 23/24 个有
- `VAEDecode` —— 23/24 个有
- `ConditioningZeroOut` —— 20/24 个有
- `LoraLoaderModelOnly` —— 17/24 个有
- `JjkText` —— 13/24 个有
- `solarL_SaveImagesToZip` —— 13/24 个有
- `PreviewImage` —— 11/24 个有
- `LoadImage` —— 9/24 个有
- `孤海注释` —— 7/24 个有
- `QwenImage21Cache` —— 2/24 个有
- `TextEncodeQwenImage21` —— 2/24 个有
- `DualCLIPLoader` —— 1/24 个有
- `Flex2Conditioner` —— 1/24 个有
- `GetImageSize` —— 1/24 个有
- `Image Comparer (rgthree)` —— 1/24 个有
- `PromptBatchQueue` —— 1/24 个有
- `VAEDecodeTiled` —— 1/24 个有
- `VNCCS_PoseStudio` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 40 | 24 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 24 | 51% |
| 采样算法 | er_sde | - | 24 | 71% |
| 调度器 | beta | - | 24 | 54% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |
| 宽度 | 80 | 80 - 1920 | 24 | 0% |
| 高度 | 80 | 80 - 1536 | 24 | 5% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/24 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 40，24 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，24 个样本
- 采样算法 最常用 er_sde，24 个样本，一致性 71%
- 调度器 最常用 beta，24 个样本，一致性 54%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1920，24 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，24 个样本，取值分散，一致性仅 5%
- 高发问题（30/24 个样本）：Steps较低可能导致细节不足
