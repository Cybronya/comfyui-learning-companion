---
name: text_to_image_controlnet_sampler_clip_10
type: Text To Image
frequency: 6
level: strong
coverage: 0.9425
common_nodes: [ApplyEcomIDAdvanced, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, EcomIDFaceAnalysis, EcomID_PulidModelLoader, EmptyLatentImage, InstantIDModelLoader, KSampler, LoadImage, PulidEvaClipLoader, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/Q版3D数字人_1910990868789063681.json, 图片生成/图生图/指定人物3D数字人Q版_1931674249235509249.json, 图片生成/文生图/文生图EcomID-基础模仿脸部_1916150458388516866.json, 平台全量/CG迷-EcomID人物换脸工作流_1927059461561810945.json, 平台全量/Ecomid_换脸_1881978366642225153.json, 平台全量/真人照片转3D定制Q版卡通形象徽章_1954379379096875010.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Q版3D数字人_1910990868789063681.json、图片生成/图生图/指定人物3D数字人Q版_1931674249235509249.json、图片生成/文生图/文生图EcomID-基础模仿脸部_1916150458388516866.json、平台全量/CG迷-EcomID人物换脸工作流_1927059461561810945.json、平台全量/Ecomid_换脸_1881978366642225153.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `ApplyEcomIDAdvanced`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EcomIDFaceAnalysis`
- `EcomID_PulidModelLoader`
- `EmptyLatentImage`
- `InstantIDModelLoader`
- `KSampler`
- `LoadImage`
- `PulidEvaClipLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 2/6 个有
- `FaceAnalysisModels` —— 2/6 个有
- `FaceBoundingBox` —— 2/6 个有
- `LoraLoader` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `ImageResize+` —— 1/6 个有
- `VAEEncode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1024 | 6 | 87% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| 采样步数 | 25 | 25 - 26 | 6 | 98% |
| Prompt 约束强度(CFG) | 6 | 2 - 6 | 6 | 68% |
| 采样算法 | dpmpp_2m | - | 6 | 67% |
| 调度器 | karras | - | 6 | 100% |
| 重绘幅度 | 1 | 0.6 - 1 | 6 | 84% |
| LoRA 模型强度 | 0.2 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1024，6 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 26，6 个样本，取值集中（一致性 98%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 2 - 6，6 个样本
- 采样算法 最常用 dpmpp_2m，6 个样本，一致性 67%
- 调度器 最常用 karras，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，6 个样本，取值集中（一致性 84%）
- LoRA 模型强度 中位数 0.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
