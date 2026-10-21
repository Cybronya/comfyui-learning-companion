---
name: unknown_workflow_video_lora_sampler_169
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.894818
common_nodes: [CreateCFGScheduleFloatList, Float, INTConstant, JWInteger, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2066681308595712001.json, 视频生成/图生视频/2055171452390912002.json, 视频生成/图生视频/1982245487325659137.json, 视频生成/图生视频/1982131363547619329.json, 视频生成/图生视频/1984923228604940289.json, 视频生成/图生视频/2026898938053271554.json, 视频生成/图生视频/1976156125466902529.json, 视频生成/图生视频/1980903199232184321.json, 视频生成/图生视频/1978368090293555201.json, 视频生成/图生视频/1980273017576185857.json, 视频生成/文生视频/1968636624055750658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_169

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2066681308595712001.json、视频生成/图生视频/2055171452390912002.json、视频生成/图生视频/1982245487325659137.json、视频生成/图生视频/1982131363547619329.json、视频生成/图生视频/1984923228604940289.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `Float`
- `INTConstant`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 10/11 个有
- `GetImageSizeAndCount` —— 10/11 个有
- `WanVideoTorchCompileSettings` —— 10/11 个有
- `HunyuanVideoFoley` —— 9/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/11 个有
- `LoadImage` —— 9/11 个有
- `SaveLatent` —— 9/11 个有
- `VAEEncode` —— 9/11 个有
- `VAELoader` —— 9/11 个有
- `WanVideoImageToVideoEncode` —— 9/11 个有
- `easy showAnything` —— 8/11 个有
- `text_mul_replace` —— 7/11 个有
- `ImageFromBatch+` —— 2/11 个有
- `LayerUtility: PurgeVRAM` —— 2/11 个有
- `LayerUtility: PurgeVRAM V2` —— 2/11 个有
- `StringToFloatList` —— 2/11 个有
- `WanVideoEmptyEmbeds` —— 2/11 个有
- `easy batchAnything` —— 2/11 个有
- `AILab_QwenVL` —— 1/11 个有
- `RH_LLMAPI_NODE` —— 1/11 个有
- `math_calculate` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
