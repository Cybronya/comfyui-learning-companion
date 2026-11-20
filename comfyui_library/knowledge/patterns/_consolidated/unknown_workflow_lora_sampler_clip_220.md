---
name: unknown_workflow_lora_sampler_clip_220
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.953333
common_nodes: [CLIPLoader, CLIPTextEncode, Int, KSamplerAdvanced, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Wan2.2文生视频4步极速版_2043282712538128386.json, 视频生成/图生视频/wan2.2-Camera运镜控制_1968658740180340737.json, 视频生成/文生视频/wan2.2文生视频4steps加速官方版_2028309492064063490.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_220

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Wan2.2文生视频4步极速版_2043282712538128386.json、视频生成/图生视频/wan2.2-Camera运镜控制_1968658740180340737.json、视频生成/文生视频/wan2.2文生视频4steps加速官方版_2028309492064063490.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Int`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 2/3 个有
- `EmptyHunyuanLatentVideo` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `CreateVideo` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `WanCameraEmbedding` —— 1/3 个有
- `WanCameraImageToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
