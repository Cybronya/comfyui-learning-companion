---
name: unknown_workflow_sampler_clip_unet_172
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.913875
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux1-dev-fp8与flux1-dev-Q4模型对比_1836327501579841537.json, 图片生成/文生图/flux文生图(自用）_1891744030592774146.json, 图片生成/文生图/flux文生图_1896040375998414850.json, 图片生成/文生图/flux文生图_1896043053692092417.json, 图片生成/文生图/flux生图工作流_1946106579613609985.json, 图片生成/文生图/小红书生活FLUX一键生成极致逼真美女—comfyui工作流_1957765376640909314.json, 图片生成/文生图/文生四宫格图_1908149869620375554.json, 图片生成/文生图/文生四宫格图_2060284327476416514.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_172

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/flux1-dev-fp8与flux1-dev-Q4模型对比_1836327501579841537.json、图片生成/文生图/flux文生图(自用）_1891744030592774146.json、图片生成/文生图/flux文生图_1896040375998414850.json、图片生成/文生图/flux文生图_1896043053692092417.json、图片生成/文生图/flux生图工作流_1946106579613609985.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/8 个有
- `EmptyLatentImage` —— 5/8 个有
- `FluxGuidance` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `UnetLoaderGGUF` —— 3/8 个有
- `CheckpointLoaderSimple` —— 2/8 个有
- `EmptySD3LatentImage` —— 2/8 个有
- `ModelSamplingFlux` —— 2/8 个有
- `DualCLIPLoaderGGUF` —— 1/8 个有
- `ImageCrop+` —— 1/8 个有
- `RandomPrompt` —— 1/8 个有
- `SDXLEmptyLatentSizePicker+` —— 1/8 个有
- `StringFunction|pysssss` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1448 | 5 | 70% |
| 高度 | 1024 | 1 - 1920 | 6 | 38% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1448，5 个样本
- 高度 中位数 1024，观测区间 1 - 1920，6 个样本，取值分散，一致性仅 38%
