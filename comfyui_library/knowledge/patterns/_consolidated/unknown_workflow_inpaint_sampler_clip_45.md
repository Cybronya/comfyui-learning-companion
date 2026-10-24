---
name: unknown_workflow_inpaint_sampler_clip_45
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.906333
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/wan视频模型修手工作流更加真实（高射炮打蚊子系列二）_1945432740814626817.json, 图片生成/图生图/手脚_面部修复_1986304182204452865.json, 图片生成/图生图/🐝【大炮工具】wan修手修脚修身工作流🐝_1945359817273954306.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/wan视频模型修手工作流更加真实（高射炮打蚊子系列二）_1945432740814626817.json、图片生成/图生图/手脚_面部修复_1986304182204452865.json、图片生成/图生图/🐝【大炮工具】wan修手修脚修身工作流🐝_1945359817273954306.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 2/3 个有
- `ModelSamplingSD3` —— 2/3 个有
- `LayerMask: MaskGrow` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `easy float` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 10 - 12 | 3 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.35 | 0.18 - 0.35 | 3 | 73% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，观测区间 10 - 12，3 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.35，观测区间 0.18 - 0.35，3 个样本
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
