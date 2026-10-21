---
name: text_to_image_sampler_clip_unet_5
type: Text To Image
frequency: 22
level: weak
coverage: 0.914455
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/【开箱即用】KREA-2-FP8_文生图基础流_新任生图王者_风格万变_2069375033096622081.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_V2版_2105216145447014402.json, 图片生成/文生图/【老金驿站】Anima二次元专属出图工作流_2019258717857914882.json, 图片生成/文生图/【通义-ZImage文生图】最强小参数大猛兽！ 极致速度、极致质量、极致性价比。_1994129975662100482.json, 图片生成/文生图/【遇见AI】Krea2 Lip BIting 咬嘴唇lora_2082379890434854914.json, 图片生成/文生图/【遇见AI】Krea2文生图基础工作流_2069621635891679234.json, 图片生成/文生图/【遇见AI】boogu image base基础工作流_2067907838378340354.json, 图片生成/文生图/【遇见AI】boogu image turbo 基础工作流_2067908137574813697.json, 图片生成/文生图/【阡陌】Z-Image最强极速文生图工作流_1993971431174242306.json, 图片生成/文生图/【阿良绘】boogu_turbo文生图工作流_2071226103880044545.json, 图片生成/文生图/千问qwen-image-2.1文生图_2108106051034894338.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜_2107739693239590914.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜注意仅供学习不可商用_2104770730121588737.json, 图片生成/文生图/咖啡馆漫画风文生图工作流｜动漫角色场景插图｜氛围感出图利器_2101873892548759553.json, 图片生成/文生图/图图工作流人像写真｜Krea2文生图摄影出图_2095578272632496130.json, 图片生成/文生图/图图组合文生图玩法｜Krea2 多图融合一键出图_2096264881749184513.json, 图片生成/文生图/图生图任意角度转换双图版｜Qwen Image2.1 多角度出图更立体_2105540395974348802.json, 数字人/数字人/千问大模型驱动的数字人工作流，多功能AI生成方案_2102883846000828418.json, 数字人/数字人/千问大模型驱动的数字人工作流，多功能AI生成方案_2105115732848766978.json, 视频生成/图生视频/Qwen Image 2.1参考人物姿势，图生视频姿势参考生成方案_2103578331991068673.json, 视频生成/图生视频/Qwen_Image_2.1_PE图像编辑工作流，人像写真图生图其它图片处理方案_2109526005462421506.json, 视频生成/图生视频/Remove模型Qwen_Image_2.1_PE姿势编辑工作流，人物类特效擦除图生图_2108739961490071554.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_5

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/文生图/【开箱即用】KREA-2-FP8_文生图基础流_新任生图王者_风格万变_2069375033096622081.json、图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_V2版_2105216145447014402.json、图片生成/文生图/【老金驿站】Anima二次元专属出图工作流_2019258717857914882.json、图片生成/文生图/【通义-ZImage文生图】最强小参数大猛兽！ 极致速度、极致质量、极致性价比。_1994129975662100482.json、图片生成/文生图/【遇见AI】Krea2 Lip BIting 咬嘴唇lora_2082379890434854914.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 21/22 个有
- `LoraLoaderModelOnly` —— 15/22 个有
- `ConditioningZeroOut` —— 14/22 个有
- `JjkText` —— 12/22 个有
- `solarL_SaveImagesToZip` —— 12/22 个有
- `LoadImage` —— 10/22 个有
- `PreviewImage` —— 9/22 个有
- `孤海注释` —— 7/22 个有
- `QwenImage21Cache` —— 6/22 个有
- `TextEncodeQwenImage21` —— 6/22 个有
- `ComfySwitchNode` —— 5/22 个有
- `ResolutionSelector` —— 5/22 个有
- `EmptyImage` —— 4/22 个有
- `CR Prompt Text` —— 3/22 个有
- `CR Text` —— 3/22 个有
- `QwenPERewriteT8` —— 3/22 个有
- `easy cleanGpuUsed` —— 3/22 个有
- `easy showAnything` —— 3/22 个有
- `QwenImage21BlockCacheT8` —— 2/22 个有
- `QwenImage21SageAttentionT8` —— 2/22 个有
- `QwenImage21SpectrumT8` —— 2/22 个有
- `AIO_Preprocessor` —— 1/22 个有
- `CheckpointLoaderSimple` —— 1/22 个有
- `VAEDecodeTiled` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 40 | 22 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 22 | 48% |
| 采样算法 | er_sde | - | 22 | 73% |
| 调度器 | beta | - | 22 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 80 | 80 - 1920 | 22 | 0% |
| 高度 | 80 | 80 - 1920 | 22 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/22 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 40，22 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，22 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 er_sde，22 个样本，一致性 73%
- 调度器 最常用 beta，22 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1920，22 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，22 个样本，取值分散，一致性仅 0%
- 高发问题（22/22 个样本）：Steps较低可能导致细节不足
