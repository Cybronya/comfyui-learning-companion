---
name: image_to_image_controlnet_ipadapter_upscale
type: Image To Image
frequency: 2
level: weak
coverage: 0.909
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, IPAdapterAdvanced, IPAdapterModelLoader, Image Save, KSampler, KSamplerSelect, LoadImage, OpenposePreprocessor, PreviewImage, RandomNoise, SDXLEmptyLatentSizePicker+, SamplerCustomAdvanced, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux 人物一致性，多视角人物_1915228748579540994.json, 图片生成/图生图/flux人物多视角一键生成_1917156480104206337.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_upscale

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux 人物一致性，多视角人物_1915228748579540994.json、图片生成/图生图/flux人物多视角一键生成_1917156480104206337.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `IPAdapterAdvanced`
- `IPAdapterModelLoader`
- `Image Save`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `OpenposePreprocessor`
- `PreviewImage`
- `RandomNoise`
- `SDXLEmptyLatentSizePicker+`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| 宽度 | 1216x832 (1.46) | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 最常用 1216x832 (1.46)，2 个样本，一致性 100%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
