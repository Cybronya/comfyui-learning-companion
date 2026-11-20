---
name: unknown_workflow_video_lora_sampler_763
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.930333
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, TrimVideoLatent, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo]
problems: []
missing: []
members: [视频生成/图生视频/电商产品展示 固定模特  视频版_1985965046280986626.json, 视频生成/图生视频/首尾帧Wan2.2 Fun VACE_1971104908562862081.json, 视频生成/文生视频/Wan 2.2-Fun-VACE-图生视频_1967620116848545793.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_763

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/电商产品展示 固定模特  视频版_1985965046280986626.json、视频生成/图生视频/首尾帧Wan2.2 Fun VACE_1971104908562862081.json、视频生成/文生视频/Wan 2.2-Fun-VACE-图生视频_1967620116848545793.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `DiffusionModelLoaderKJ` —— 2/3 个有
- `DiffusionModelSelector` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `WanVideoVACEStartToEndFrame` —— 2/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `ImageRepeat` —— 1/3 个有
- `ImpactFloat` —— 1/3 个有
- `Text` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `ZML_DualInteger` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 6 - 16 | 3 | 57% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | lcm | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 16，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 16，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
