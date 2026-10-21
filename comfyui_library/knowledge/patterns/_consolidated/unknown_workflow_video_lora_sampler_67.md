---
name: unknown_workflow_video_lora_sampler_67
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.971944
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1906002583012429826.json, 视频生成/图生视频/1946216750084186114.json, 视频生成/图生视频/1900096506861608962.json, 视频生成/图生视频/1902955748278571009.json, 视频生成/图生视频/1899859453431406594.json, 视频生成/图生视频/1899879062079430658.json, 视频生成/图生视频/1901478845646520322.json, 视频生成/图生视频/1899855104164651009.json, 视频生成/图生视频/1899813339864915970.json, 视频生成/图生视频/1901473819838529538.json, 视频生成/图生视频/1919259091414220801.json, 视频生成/图生视频/1900918919576854530.json, 视频生成/图生视频/1900758531451297794.json, 视频生成/图生视频/1900041453022621698.json, 视频生成/图生视频/1913149294990557186.json, 视频生成/图生视频/1964345936161947649.json, 视频生成/图生视频/2011643164708315137.json, 视频生成/图生视频/1937393290176045057.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_67

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/1906002583012429826.json、视频生成/图生视频/1946216750084186114.json、视频生成/图生视频/1900096506861608962.json、视频生成/图生视频/1902955748278571009.json、视频生成/图生视频/1899859453431406594.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 18 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTeaCache` —— 16/18 个有
- `Int` —— 15/18 个有
- `WanVideoEnhanceAVideo` —— 13/18 个有
- `ImageResizeKJ` —— 12/18 个有
- `TextInput_` —— 12/18 个有
- `RIFE VFI` —— 9/18 个有
- `ImageScaleToTotalPixels` —— 6/18 个有
- `easy imageSize` —— 6/18 个有
- `WanVideoSLG` —— 5/18 个有
- `CR Upscale Image` —— 4/18 个有
- `CR Text` —— 3/18 个有
- `CogVideoEnhanceAVideo` —— 3/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/18 个有
- `MathExpression|pysssss` —— 3/18 个有
- `PreviewImage` —— 3/18 个有
- `Fast Groups Bypasser (rgthree)` —— 2/18 个有
- `WanVideoContextOptions` —— 2/18 个有
- `easy int` —— 2/18 个有
- `CR Text Concatenate` —— 1/18 个有
- `RH_Captioner` —— 1/18 个有
- `ShowText|pysssss` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
