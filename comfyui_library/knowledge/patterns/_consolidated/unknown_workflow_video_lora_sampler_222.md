---
name: unknown_workflow_video_lora_sampler_222
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.968667
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1902338359216484353.json, 视频生成/图生视频/1907459006556999682.json, 视频生成/图生视频/1899781896895881218.json, 视频生成/图生视频/2079036262153023489.json, 视频生成/图生视频/1899122164795133953.json, 视频生成/图生视频/1899508208174809089.json, 视频生成/图生视频/1899811031231639553.json, 视频生成/图生视频/1914559831519494146.json, 视频生成/图生视频/1914130917185548290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_222

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1902338359216484353.json、视频生成/图生视频/1907459006556999682.json、视频生成/图生视频/1899781896895881218.json、视频生成/图生视频/2079036262153023489.json、视频生成/图生视频/1899122164795133953.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 8/9 个有
- `WanVideoTextEncode` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `WanVideoTeaCache` —— 7/9 个有
- `Textbox` —— 5/9 个有
- `LayerUtility: PurgeVRAM` —— 3/9 个有
- `WanVideoEnhanceAVideo` —— 3/9 个有
- `GetImageSizeAndCount` —— 2/9 个有
- `Note Plus (mtb)` —— 2/9 个有
- `WanVideoTorchCompileSettings` —— 2/9 个有
- `SaveLatent` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有
- `TextBox` —— 1/9 个有
- `workflow>文本` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
