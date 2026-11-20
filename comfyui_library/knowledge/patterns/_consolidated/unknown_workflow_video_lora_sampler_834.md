---
name: unknown_workflow_video_lora_sampler_834
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.888333
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [平台全量/长视频连续生成：Wan2.2 14B+LightX2V 12步超极速高质量视频连续生视频V1_1959621304016121857.json, 视频生成/图生视频/90秒81帧6步超极速图生视频_1995392959409479682.json, 视频生成/图生视频/AA--金子雨特效lora-wan2.2 加速图生视频+独立放大插帧_2003814653497122818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_834

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/长视频连续生成：Wan2.2 14B+LightX2V 12步超极速高质量视频连续生视频V1_1959621304016121857.json、视频生成/图生视频/90秒81帧6步超极速图生视频_1995392959409479682.json、视频生成/图生视频/AA--金子雨特效lora-wan2.2 加速图生视频+独立放大插帧_2003814653497122818.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Image Size to Number` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `Int` —— 1/3 个有
- `SomethingToString` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `VHS_MergeImages` —— 1/3 个有
- `VHS_SelectImages` —— 1/3 个有
- `easy mathInt` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 6 | 6 - 12 | 3 | 65% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | lcm | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 12，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
