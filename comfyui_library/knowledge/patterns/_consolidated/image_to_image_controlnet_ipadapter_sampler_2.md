---
name: image_to_image_controlnet_ipadapter_sampler_2
type: Image To Image
frequency: 18
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, CR SDXL Aspect Ratio, CheckpointLoaderSimple, ControlNetLoader, DualCLIPLoader, Float, FluxGuidance, IPAdapterUnifiedLoader, ImageGenResolutionFromImage, Int, JanusImageUnderstanding, JanusModelLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, RHHiddenNodes, SaveImage, Solarize, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/反推提示词/49xiangaoshangse_2050141393024241665.json, 图片生成/图生图/[邪修一键上色]（可指定风格）_2019243811410550786.json, 图片生成/图生图/【保姆级】线稿上色，指定参考风格上色_2005940936268021762.json, 图片生成/图生图/【保姆级】线稿上色，指定参考风格上色_2014518255880245250.json, 图片生成/图生图/【保姆级】线稿上色，指定参考风格上色_2039158230911295490.json, 图片生成/图生图/【保姆级】线稿上色，指定参考风格上色_2046438463171469314.json, 图片生成/图生图/【保姆级】线稿上色，指定参考风格上色_2059903565107388418.json, 图片生成/图生图/【保姆级】线稿上色，指定参考风格上色_2059992136216563713.json, 图片生成/图生图/【保姆级】线稿上色，指定参考风格上色_2096869080191037441.json, 图片生成/图生图/保姆级线稿上色，风格任你指定，轻松让你的线稿更“灵动鲜活”~_2011339442941861889.json, 图片生成/图生图/保姆级线稿上色，风格任你指定，轻松让你的线稿更“灵动鲜活”~_2046403784745689089.json, 图片生成/图生图/线稿上色，指定参考风格上色_2043650615166898177.json, 图片生成/图生图/线稿指定色彩风格上色_2028368289763696641.json, 图片生成/图生图/线稿指定风格上色_2009522063400243202.json, 图片生成/图生图/（超丝滑）线稿指定色彩风格上色_2047576234992865281.json, 平台全量/【保姆级】线稿上色_2035881913793122306.json, 平台全量/【保姆级】线稿上色，指定参考风格上色_2096511281623814146.json, 平台全量/智能线稿上色，指定参考风格上色+高清放大_2047582132247203842.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_sampler_2

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/反推提示词/49xiangaoshangse_2050141393024241665.json、图片生成/图生图/[邪修一键上色]（可指定风格）_2019243811410550786.json、图片生成/图生图/【保姆级】线稿上色，指定参考风格上色_2005940936268021762.json、图片生成/图生图/【保姆级】线稿上色，指定参考风格上色_2014518255880245250.json、图片生成/图生图/【保姆级】线稿上色，指定参考风格上色_2039158230911295490.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `DualCLIPLoader`
- `Float`
- `FluxGuidance`
- `IPAdapterUnifiedLoader`
- `ImageGenResolutionFromImage`
- `Int`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `RHHiddenNodes`
- `SaveImage`
- `Solarize`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `RTXVideoSuperResolution` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 18 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 18 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 18 | 100% |
| 调度器 | karras | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，18 个样本，一致性 100%
- 调度器 最常用 karras，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
