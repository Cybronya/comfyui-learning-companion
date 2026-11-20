---
name: image_to_image_sampler_clip_checkpoint_3
type: Image To Image
frequency: 7
level: strong
coverage: 0.842571
common_nodes: [BackgroundScaler, CLIPTextEncode, CheckpointLoaderSimple, ICLightConditioning, KSampler, LoadAndApplyICLightUnet, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/IC-Light一键换背景（带光源）_1915330754077986817.json, 图片生成/图生图/Prompt 修图 换背景 + 重新打光_1922168228884447234.json, 图片生成/图生图/【简易版】自动匹配光源 ｜一键换背景_1915388396548587521.json, 图片生成/图生图/任意人像换背景+打光_1915022890402574337.json, 图片生成/图生图/换背景+匹配光效(简易版）1_1900359646790545409.json, 图片生成/图生图/超级简单 自动匹配光源 ＋一键换背景_2028303079195545601.json, 平台全量/CG迷-产品换背景+匹配光效工作流_1927036000055492609.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/IC-Light一键换背景（带光源）_1915330754077986817.json、图片生成/图生图/Prompt 修图 换背景 + 重新打光_1922168228884447234.json、图片生成/图生图/【简易版】自动匹配光源 ｜一键换背景_1915388396548587521.json、图片生成/图生图/任意人像换背景+打光_1915022890402574337.json、图片生成/图生图/换背景+匹配光效(简易版）1_1900359646790545409.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `BackgroundScaler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ICLightConditioning`
- `KSampler`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `DetailTransfer` —— 6/7 个有
- `LightSource` —— 6/7 个有
- `easy imageSize` —— 6/7 个有
- `GroundingDinoModelLoader (segment anything)` —— 4/7 个有
- `GroundingDinoSAMSegment (segment anything)` —— 4/7 个有
- `SAMModelLoader (segment anything)` —— 4/7 个有
- `Anything Everywhere` —— 3/7 个有
- `LoraLoader` —— 3/7 个有
- `easy imageRemBg` —— 3/7 个有
- `easy ipadapterApply` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 7 | 91% |
| Prompt 约束强度(CFG) | 2 | 2 - 2.5 | 7 | 89% |
| 采样算法 | dpmpp_2m_sde | - | 7 | 100% |
| 调度器 | karras | - | 7 | 100% |
| 重绘幅度 | 0.9 | 0.9 - 0.9 | 7 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，7 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 2.5，7 个样本，取值集中（一致性 89%）
- 采样算法 最常用 dpmpp_2m_sde，7 个样本，一致性 100%
- 调度器 最常用 karras，7 个样本，一致性 100%
- 重绘幅度 中位数 0.9，观测区间 0.9 - 0.9，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
