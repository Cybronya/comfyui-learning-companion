---
name: unknown_workflow_video_lora_sampler_288
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.946
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/Wan2.2文生视频4步极速版_2043282712538128386.json, 视频生成/图生视频/Wan2.2 14B 首尾帧_1968955228710133762.json, 视频生成/图生视频/Wan2.2_首尾帧视频_4步极速版_ComfyUI官方流_2017568784646672385.json, 视频生成/图生视频/Wan2.2首尾帧工作流ComfyUI官方流_2050472487972032513.json, 视频生成/图生视频/smooth首尾帧图生视频工作流_2067255627071709185.json, 视频生成/图生视频/首尾帧图生视频工作流_2066470344814321666.json, 视频生成/图生视频/首尾帧图生视频社区模型Smooth Mix i2V v2.0工作流_2050542650729746434.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_288

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Wan2.2文生视频4步极速版_2043282712538128386.json、视频生成/图生视频/Wan2.2 14B 首尾帧_1968955228710133762.json、视频生成/图生视频/Wan2.2_首尾帧视频_4步极速版_ComfyUI官方流_2017568784646672385.json、视频生成/图生视频/Wan2.2首尾帧工作流ComfyUI官方流_2050472487972032513.json、视频生成/图生视频/smooth首尾帧图生视频工作流_2067255627071709185.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `WanFirstLastFrameToVideo` —— 6/7 个有
- `ImageResize+` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `easy showAnything` —— 3/7 个有
- `Int` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `CM_IntToFloat` —— 1/7 个有
- `EmptyHunyuanLatentVideo` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 57% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 7 | 75% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，7 个样本
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
