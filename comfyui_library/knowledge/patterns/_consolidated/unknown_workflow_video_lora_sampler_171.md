---
name: unknown_workflow_video_lora_sampler_171
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.946
common_nodes: [CreateCFGScheduleFloatList, INTConstant, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Work-Fisher_Wan2.2-I2V增强版_1972312939401310209.json, 视频生成/图生视频/gen全能视频Si-wan2.2首尾帧kijai版_1952803879810494466.json, 视频生成/图生视频/kijai-Wan2.2首尾帧+过渡帧_1963047092535136257.json, 视频生成/图生视频/wan 2.2 冰冻视频特效_1953012198424702978.json, 视频生成/图生视频/wan2.2图生视频(KJ版)_1951528284905525250.json, 视频生成/图生视频/wan2.2图生视频首尾帧（KJ版）_1955148796940488705.json, 视频生成/图生视频/wan2.2图生视频（KJ流）加速_1950178102964084737.json, 视频生成/图生视频/冰天雪地视频特效_2004446571733417986.json, 视频生成/图生视频/视频-Wan2.2首尾帧+过渡帧_1978365294227906562.json, 视频生成/图生视频/通义万相WAN2.2_KJ加速版_高低噪声双lora在线本地通用_补帧_1952913426868858882.json, 视频生成/图生视频/通义万相WAN2.2_KJ加速版_高噪声lora在线本地通用_补帧_1952709897437777921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_171

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Work-Fisher_Wan2.2-I2V增强版_1972312939401310209.json、视频生成/图生视频/gen全能视频Si-wan2.2首尾帧kijai版_1952803879810494466.json、视频生成/图生视频/kijai-Wan2.2首尾帧+过渡帧_1963047092535136257.json、视频生成/图生视频/wan 2.2 冰冻视频特效_1953012198424702978.json、视频生成/图生视频/wan2.2图生视频(KJ版)_1951528284905525250.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 10/11 个有
- `ImageResizeKJv2` —— 10/11 个有
- `WanVideoSetBlockSwap` —— 10/11 个有
- `WanVideoSetLoRAs` —— 10/11 个有
- `WanVideoTorchCompileSettings` —— 9/11 个有
- `Int` —— 4/11 个有
- `RIFE VFI` —— 4/11 个有
- `CLIPVisionLoader` —— 2/11 个有
- `Fast Groups Muter (rgthree)` —— 2/11 个有
- `RH_Translator` —— 2/11 个有
- `ShowText|pysssss` —— 2/11 个有
- `WanVideoClipVisionEncode` —— 2/11 个有
- `WanVideoContextOptions` —— 2/11 个有
- `WanVideoEncodeLatentBatch` —— 2/11 个有
- `WanVideoTeaCache` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
