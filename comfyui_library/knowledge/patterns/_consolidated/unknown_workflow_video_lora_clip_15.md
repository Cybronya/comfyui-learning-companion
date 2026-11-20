---
name: unknown_workflow_video_lora_clip_15
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.717667
common_nodes: [CLIPLoader, CLIPTextEncode, ImageScale, InstructPixToPixConditioning, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/【Wan2.1系列】深度控制Depth工作流_1919378897581051906.json, 平台全量/【Wan2.1系列】高清放大Tile工作流_1919416956456472578.json, 视频生成/图生视频/Wan2.1深度控制视频迁移和重绘_1903507443177918465.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_15

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/【Wan2.1系列】深度控制Depth工作流_1919378897581051906.json、平台全量/【Wan2.1系列】高清放大Tile工作流_1919416956456472578.json、视频生成/图生视频/Wan2.1深度控制视频迁移和重绘_1903507443177918465.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageScale`
- `InstructPixToPixConditioning`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 2/3 个有
- `DepthAnythingV2Preprocessor` —— 2/3 个有
- `KSamplerSelect` —— 2/3 个有
- `SamplerCustom` —— 2/3 个有
- `SplitSigmas` —— 2/3 个有
- `ImageBlur` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `Primitive string [Crystools]` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Text Concatenate (JPS)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 1 | 100% |
| 采样算法 | uni_pc | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
