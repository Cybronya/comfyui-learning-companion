---
name: unknown_workflow_video_lora_sampler_302
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.909143
common_nodes: [CR Text, CreateCFGScheduleFloatList, Float, GetImageSizeAndCount, INTConstant, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, ShowText|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1972840899115982849.json, 视频生成/图生视频/1978395931462750209.json, 视频生成/图生视频/1983384271719178241.json, 视频生成/图生视频/1997296684856184833.json, 视频生成/图生视频/1950857744138043393.json, 视频生成/图生视频/1986614260161802241.json, 视频生成/图生视频/2000608188644851714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_302

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1972840899115982849.json、视频生成/图生视频/1978395931462750209.json、视频生成/图生视频/1983384271719178241.json、视频生成/图生视频/1997296684856184833.json、视频生成/图生视频/1950857744138043393.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CR Text`
- `CreateCFGScheduleFloatList`
- `Float`
- `GetImageSizeAndCount`
- `INTConstant`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 6/7 个有
- `PrimitiveInt` —— 6/7 个有
- `PrimitiveString` —— 6/7 个有
- `RHHiddenNodes` —— 6/7 个有
- `SimpleMath+` —— 6/7 个有
- `Wan22PromptSelector` —— 6/7 个有
- `WanVideoLoraSelect` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `easy anythingIndexSwitch` —— 6/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 5/7 个有
- `GIMMVFI_interpolate` —— 5/7 个有
- `CR Text Concatenate` —— 1/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `RH_Captioner` —— 1/7 个有
- `WanVideoLoraSelectMulti` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
