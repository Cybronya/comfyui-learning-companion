---
name: unknown_workflow_video_lora_sampler_553
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8995
common_nodes: [CreateCFGScheduleFloatList, FastUnsharpSharpen, INTConstant, JWInteger, PrimitiveFloat, SaveImage, Seed (rgthree), TT_img_enc, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: [Seed (rgthree), CR Prompt Text]
members: [视频生成/文生视频/1974785669753081858.json, 视频生成/文生视频/1974792625356148738.json, 视频生成/文生视频/1975846186269675522.json, 视频生成/文生视频/1975847976218308609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_553

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/1974785669753081858.json、视频生成/文生视频/1974792625356148738.json、视频生成/文生视频/1975846186269675522.json、视频生成/文生视频/1975847976218308609.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `FastUnsharpSharpen`
- `INTConstant`
- `JWInteger`
- `PrimitiveFloat`
- `SaveImage`
- `Seed (rgthree)`
- `TT_img_enc`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `LoadImage` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `WanVideoLoraSelect` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Seed (rgthree)、CR Prompt Text
