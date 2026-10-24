---
name: unknown_workflow_video_lora_sampler_940
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.86
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Replace, EmptyHunyuanLatentVideo, INTConstant, ImageFromBatch+, ImageSharpen, Int, JjkText, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveBoolean, RH_Prompter, ShowText, SimpleMath+, TextBox, TorchCompileModel, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy ifElse]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2 HoloCine-无限时长-电影多镜头文生视频-自动提示词_1983679735324712962.json, 视频生成/文生视频/Wan2.2 HoloCine-无限时长-电影多镜头文生视频_1984439395342303234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_940

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 HoloCine-无限时长-电影多镜头文生视频-自动提示词_1983679735324712962.json、视频生成/文生视频/Wan2.2 HoloCine-无限时长-电影多镜头文生视频_1984439395342303234.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Replace`
- `EmptyHunyuanLatentVideo`
- `INTConstant`
- `ImageFromBatch+`
- `ImageSharpen`
- `Int`
- `JjkText`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `RH_Prompter`
- `ShowText`
- `SimpleMath+`
- `TextBox`
- `TorchCompileModel`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy ifElse`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 10 | - | 2 | 100% |
| 采样算法 | 4 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
