---
name: unknown_workflow_video_lora_sampler_823
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.961
common_nodes: [CLIPLoader, CLIPTextEncode, ImageScale, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveStringMultiline, QZ_ResolutionPreset, TextInput_, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG, easy int]
problems: []
missing: []
members: [平台全量/万相wan2.2视频图像驱动 B站：乔治-周士诚_1957370684315987969.json, 视频生成/图生视频/万相wan2.2 图生视频 B站：乔治-周士诚_1957316699274014721.json, 视频生成/图生视频/万相wan2.2 首尾帧 B站：乔治-周士诚_1957365493348888578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_823

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/万相wan2.2视频图像驱动 B站：乔治-周士诚_1957370684315987969.json、视频生成/图生视频/万相wan2.2 图生视频 B站：乔治-周士诚_1957316699274014721.json、视频生成/图生视频/万相wan2.2 首尾帧 B站：乔治-周士诚_1957365493348888578.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageScale`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveStringMultiline`
- `QZ_ResolutionPreset`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 1/3 个有
- `DepthAnythingV2Preprocessor` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `Wan22FunControlToVideo` —— 1/3 个有
- `WanFirstLastFrameToVideo` —— 1/3 个有
- `WanImageToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
