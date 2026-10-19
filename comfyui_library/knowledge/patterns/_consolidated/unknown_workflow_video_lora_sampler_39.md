---
name: unknown_workflow_video_lora_sampler_39
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.833696
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, JWInteger, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [CR Prompt Text]
members: [视频生成/文生视频/1964924575370854402.json, 视频生成/文生视频/1964929046893182977.json, 视频生成/文生视频/1964934510620102657.json, 视频生成/文生视频/1964929542555095041.json, 视频生成/文生视频/1964927799280680961.json, 视频生成/文生视频/1964919503211610114.json, 视频生成/文生视频/1964931561881747457.json, 视频生成/文生视频/1950141714336014337.json, 视频生成/文生视频/1950148142277771266.json, 视频生成/文生视频/1950200316404916225.json, 视频生成/文生视频/1950154187399192578.json, 视频生成/文生视频/1950159020893061122.json, 视频生成/文生视频/1950180748268584962.json, 视频生成/文生视频/1950165203683033089.json, 视频生成/文生视频/1950205913674244097.json, 视频生成/文生视频/1950086334457274370.json, 视频生成/文生视频/1970702549865164802.json, 视频生成/文生视频/(Palingenesis版)Wan2.2 文生视频高动态加速版V1_1972111273070620674.json, 视频生成/文生视频/1972489940305113089.json, 视频生成/文生视频/1971180956935720962.json, 视频生成/文生视频/1969009834282655745.json, 视频生成/文生视频/1966009360197521409.json, 视频生成/文生视频/（自用）KJ版节点套件视频Latent 示范工作流V1_2007518843018678273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_39

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/文生视频/1964924575370854402.json、视频生成/文生视频/1964929046893182977.json、视频生成/文生视频/1964934510620102657.json、视频生成/文生视频/1964929542555095041.json、视频生成/文生视频/1964927799280680961.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 23 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 22/23 个有
- `WanVideoTorchCompileSettings` —— 22/23 个有
- `Float` —— 14/23 个有
- `WanVideoScheduler` —— 14/23 个有
- `WanVideoSigmaToStep` —— 14/23 个有
- `Fast Groups Bypasser (rgthree)` —— 8/23 个有
- `SaveLatent` —— 3/23 个有
- `VAEEncode` —— 3/23 个有
- `VAELoader` —— 3/23 个有
- `HunyuanVideoFoley` —— 2/23 个有
- `LoadImage` —— 2/23 个有
- `SaveImage` —— 2/23 个有
- `easy showAnything` —— 2/23 个有
- `text_mul_replace` —— 2/23 个有
- `ImageFromBatch+` —— 1/23 个有
- `TT_img_enc` —— 1/23 个有
- `VAEDecode` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text
