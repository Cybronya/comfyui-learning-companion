---
name: text_to_image_lora_sampler_clip_599
type: Text To Image
frequency: 2
level: weak
coverage: 0.9305
common_nodes: [CLIPTextEncode, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, Florence2Run, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, Text Concatenate (JPS), TextInput_, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/图生图 260526_2062013169140326401.json, 图片生成/文生图/Florence2 反推提示词 + FLUX文生图工作流_1920882086809636866.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_599

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图生图 260526_2062013169140326401.json、图片生成/文生图/Florence2 反推提示词 + FLUX文生图工作流_1920882086809636866.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Florence2Run`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Text Concatenate (JPS)`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ApplyFirstBlockCachePatchAdvanced` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `Florence2ModelLoader` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `PMRF` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 688 | - | 2 | 51% |
| 高度 | 1392 | - | 2 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 688，样本不足，未给区间，2 个样本
- 高度 中位数 1392，样本不足，未给区间，2 个样本，取值集中（一致性 90%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
