---
name: unknown_workflow_video_lora_sampler_725
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.882333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DF_Integer, ImageStitch, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, RH_Translator, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, WanVideoNAG, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2首尾帧—官方优化版_1954885586667520002.json, 视频生成/图生视频/wan2.2_14B_首尾帧视频-8步加速版-自动提示词_1952219642674753538.json, 视频生成/图生视频/wan2.2首尾帧【高清输出+Foley音效】_1970093575075733506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_725

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2首尾帧—官方优化版_1954885586667520002.json、视频生成/图生视频/wan2.2_14B_首尾帧视频-8步加速版-自动提示词_1952219642674753538.json、视频生成/图生视频/wan2.2首尾帧【高清输出+Foley音效】_1970093575075733506.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DF_Integer`
- `ImageStitch`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `RH_Translator`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `WanVideoNAG`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `Textbox` —— 2/3 个有
- `easy ifElse` —— 2/3 个有
- `CR Image Size` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `CustomAddLabel` —— 1/3 个有
- `Float` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `HunyuanVideoFoley` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `NormalizeAudioLoudness` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 4 | 1 - 4 | 3 | 53% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 4，观测区间 1 - 4，3 个样本
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
