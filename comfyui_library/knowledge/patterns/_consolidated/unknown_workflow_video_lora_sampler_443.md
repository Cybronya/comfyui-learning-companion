---
name: unknown_workflow_video_lora_sampler_443
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9666
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/动漫_真人 图生视频（超级加速版）_1949636462812778497.json, 视频生成/图生视频/手办360度产品展示(wan2.1图生视频5s)_1900406595552014337.json, 视频生成/图生视频/极速泼水变装特效可灵同款wan2.1+accvid_1930526505158496258.json, 视频生成/图生视频/极速泼水变装特效可灵同款wan2.1+accvid_2018170301388955650.json, 视频生成/图生视频/（真人_动漫）图生视频（加速稳定版）_1949494090500579330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_443

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/动漫_真人 图生视频（超级加速版）_1949636462812778497.json、视频生成/图生视频/手办360度产品展示(wan2.1图生视频5s)_1900406595552014337.json、视频生成/图生视频/极速泼水变装特效可灵同款wan2.1+accvid_1930526505158496258.json、视频生成/图生视频/极速泼水变装特效可灵同款wan2.1+accvid_2018170301388955650.json、视频生成/图生视频/（真人_动漫）图生视频（加速稳定版）_1949494090500579330.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `WanVideoSLG` —— 4/5 个有
- `WanVideoTeaCache` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `CR Upscale Image` —— 2/5 个有
- `ImageSizeAndBatchSize` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `WanVideoExperimentalArgs` —— 2/5 个有
- `WanVideoMagCache` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
