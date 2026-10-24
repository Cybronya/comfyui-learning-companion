---
name: unknown_workflow_video_sampler_2
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.952067
common_nodes: [LoadImage, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode]
problems: []
missing: []
members: [图片生成/图生图/利用图片替换视频中的角色_1916038900895121410.json, 图片生成/文生图/wan2.1 高速飘移动态特效_1936223818082062337.json, 视频生成/图生视频/AccVid加速Wan-I2V图生视频_1927584684270850049.json, 视频生成/图生视频/LORA版本-FusionX图生视频_1934857703757914114.json, 视频生成/图生视频/MAGREF-吻屏kiss图生视频_2081288501450076161.json, 视频生成/图生视频/MAGREF-吻屏图生视频_2067619430019977218.json, 视频生成/图生视频/MAGREF-吻屏图生视频_2067873046999945218.json, 视频生成/图生视频/MAGREF-吻屏图生视频_2104531594294943746.json, 视频生成/图生视频/MAGREF-吻屏图生视频_2104542133922385921.json, 视频生成/图生视频/MAGREF单图参考图生视频_2026931887591133185.json, 视频生成/图生视频/MAGREF单图参考图生视频吻💋屏_2046763253136625665.json, 视频生成/图生视频/SLG 提升 WAN2.1 视频画质工作流_1919056662093561858.json, 视频生成/图生视频/Unianimate-跳舞动作迁移_1913658373089492993.json, 视频生成/图生视频/V3-专业版-完美一致性_1947143904128446465.json, 视频生成/图生视频/视频动作高度一致，超强效果！_1955563973305405442.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_2

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/利用图片替换视频中的角色_1916038900895121410.json、图片生成/文生图/wan2.1 高速飘移动态特效_1936223818082062337.json、视频生成/图生视频/AccVid加速Wan-I2V图生视频_1927584684270850049.json、视频生成/图生视频/LORA版本-FusionX图生视频_1934857703757914114.json、视频生成/图生视频/MAGREF-吻屏kiss图生视频_2081288501450076161.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 15 个 workflow 都包含：
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 14/15 个有
- `ImageResizeKJ` —— 14/15 个有
- `LoadWanVideoT5TextEncoder` —— 14/15 个有
- `WanVideoVAELoader` —— 14/15 个有
- `WanVideoBlockSwap` —— 13/15 个有
- `WanVideoModelLoader` —— 13/15 个有
- `Primitive integer [Crystools]` —— 12/15 个有
- `WanVideoLoraSelect` —— 12/15 个有
- `WanVideoTorchCompileSettings` —— 11/15 个有
- `Text Multiline` —— 10/15 个有
- `WanVideoVACEModelSelect` —— 8/15 个有
- `WanVideoSLG` —— 5/15 个有
- `ImageConcanate` —— 4/15 个有
- `VHS_LoadVideo` —— 4/15 个有
- `WanVideoUniAnimateDWPoseDetector` —— 4/15 个有
- `WanVideoUniAnimatePoseInput` —— 4/15 个有
- `PreviewImage` —— 3/15 个有
- `WanVideoExperimentalArgs` —— 3/15 个有
- `ColorMatch` —— 2/15 个有
- `GetNode` —— 2/15 个有
- `ImageFromBatch` —— 2/15 个有
- `ImpactSwitch` —— 2/15 个有
- `RHHiddenNodes` —— 2/15 个有
- `SetNode` —— 2/15 个有
- `SimpleMath+` —— 2/15 个有
- `ImageResizeKJv2` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
