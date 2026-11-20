---
name: unknown_workflow_lora_sampler_clip_258
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.889667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/文生图+图生图（超强款）Flux超强工作流_1920133263510142977.json, 图片生成/文生图/文生图+图生图（超强款）Flux超强工作流_2054447855447879682.json, 平台全量/沙雕人物四视图沙雕人物四视图加拆分_1934086916226899969.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_258

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/文生图+图生图（超强款）Flux超强工作流_1920133263510142977.json、图片生成/文生图/文生图+图生图（超强款）Flux超强工作流_2054447855447879682.json、平台全量/沙雕人物四视图沙雕人物四视图加拆分_1934086916226899969.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 2/3 个有
- `EG_FX_BDAPI` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `Joy_caption` —— 2/3 个有
- `Joy_caption_load` —— 2/3 个有
- `ttN concat` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `DepthAnythingV2Preprocessor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 1024 | 3 | 86% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| ControlNet 权重 | 0.4 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 1024，3 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
