---
name: unknown_workflow_video_lora_sampler_47
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.890048
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1972516468346777602.json, 视频生成/图生视频/1972495972968361985.json, 视频生成/图生视频/1964938797580472321.json, 视频生成/图生视频/1964944086870446082.json, 视频生成/图生视频/1964938910965055490.json, 视频生成/图生视频/1964939637061992450.json, 视频生成/图生视频/1964922517129449473.json, 视频生成/图生视频/1964962466272825346.json, 视频生成/图生视频/1964938181672095745.json, 视频生成/图生视频/1966515358914031618.json, 视频生成/图生视频/2004808833312714753.json, 视频生成/图生视频/1963292040106840066.json, 视频生成/图生视频/1976470630323326977.json, 视频生成/图生视频/1950024658970173442.json, 视频生成/图生视频/1972111264942059521.json, 视频生成/图生视频/1972564669351260162.json, 视频生成/图生视频/1971183114510864385.json, 视频生成/图生视频/1974013871881105409.json, 视频生成/图生视频/1984646206687232002.json, 视频生成/图生视频/1976203994194427906.json, 视频生成/图生视频/2073212221412438017.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_47

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/1972516468346777602.json、视频生成/图生视频/1972495972968361985.json、视频生成/图生视频/1964938797580472321.json、视频生成/图生视频/1964944086870446082.json、视频生成/图生视频/1964938910965055490.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 21 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `CR Prompt Text` —— 20/21 个有
- `Float` —— 20/21 个有
- `LoadImage` —— 20/21 个有
- `WanVideoScheduler` —— 20/21 个有
- `WanVideoSigmaToStep` —— 20/21 个有
- `WanVideoTorchCompileSettings` —— 20/21 个有
- `WanVideoSetBlockSwap` —— 19/21 个有
- `WanVideoSetLoRAs` —— 19/21 个有
- `HunyuanVideoFoley` —— 4/21 个有
- `ImageFromBatch+` —— 3/21 个有
- `LayerUtility: PurgeVRAM` —— 3/21 个有
- `SaveLatent` —— 3/21 个有
- `StringToFloatList` —— 3/21 个有
- `VAEEncode` —— 3/21 个有
- `VAELoader` —— 3/21 个有
- `easy showAnything` —— 3/21 个有
- `LayerUtility: PurgeVRAM V2` —— 2/21 个有
- `easy batchAnything` —— 2/21 个有
- `text_mul_replace` —— 2/21 个有
- `AILab_MiniCPM_4_V` —— 1/21 个有
- `AILab_QwenVL` —— 1/21 个有
- `CR Seed` —— 1/21 个有
- `Fast Groups Bypasser (rgthree)` —— 1/21 个有
- `GetNode` —— 1/21 个有
- `GetVideoComponents` —— 1/21 个有
- `LoadVideo` —— 1/21 个有
- `RH_LLMAPI_NODE` —— 1/21 个有
- `ReplaceText` —— 1/21 个有
- `SetNode` —— 1/21 个有
- `ShowText` —— 1/21 个有
- `WanVideoEmptyEmbeds` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
