---
name: unknown_workflow_video_lora_sampler_540
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.962333
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/室内设计图生视频工作流_2034129372994605057.json, 视频生成/图生视频/手办360度产品展示(wan2.1图生视频5s)_1900406595552014337.json, 视频生成/图生视频/抖起来_1997177362523570178.json, 视频生成/图生视频/接吻一镜到底丝滑舌吻_1926200490214780930.json, 视频生成/图生视频/极速泼水变装特效可灵同款wan2.1+accvid_1930526505158496258.json, 视频生成/图生视频/极速泼水变装特效可灵同款wan2.1+accvid_2018170301388955650.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_540

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/室内设计图生视频工作流_2034129372994605057.json、视频生成/图生视频/手办360度产品展示(wan2.1图生视频5s)_1900406595552014337.json、视频生成/图生视频/抖起来_1997177362523570178.json、视频生成/图生视频/接吻一镜到底丝滑舌吻_1926200490214780930.json、视频生成/图生视频/极速泼水变装特效可灵同款wan2.1+accvid_1930526505158496258.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 5/6 个有
- `WanVideoTeaCache` —— 5/6 个有
- `CR Text` —— 3/6 个有
- `WanVideoEnhanceAVideo` —— 3/6 个有
- `WanVideoTorchCompileSettings` —— 3/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `ImageSizeAndBatchSize` —— 2/6 个有
- `Int` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `WanVideoSLG` —— 2/6 个有
- `easy imageSize` —— 2/6 个有
- `Replace Text _O` —— 1/6 个有
- `SaveAnimatedWEBP` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
