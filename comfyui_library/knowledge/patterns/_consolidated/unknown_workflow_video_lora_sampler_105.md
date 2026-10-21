---
name: unknown_workflow_video_lora_sampler_105
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.874267
common_nodes: [CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [SimpleMath+, easy positive, easy seed, ImageFromBatch+, CR Prompt Text]
members: [视频生成/文生视频/1951636109178646529.json, 视频生成/文生视频/1960686158676189186.json, 视频生成/文生视频/1974801904645574658.json, 视频生成/文生视频/1978813759940628482.json, 视频生成/文生视频/1978818783190093825.json, 视频生成/文生视频/1979020058171183105.json, 视频生成/文生视频/1979736664522264578.json, 视频生成/文生视频/Wan2.2 Smooth Mix高动态文生视频V2（KJ版）_2073985473007337472.json, 视频生成/文生视频/1952329679653023745.json, 视频生成/文生视频/1950109522175115265.json, 视频生成/文生视频/（4+4步）Wan2.2 HoloCine电影多镜头文生视频（KJ版-目前效果不佳）_1982404928775831554.json, 视频生成/文生视频/（4+4步）Wan2.2 Smooth Mix V2高低噪模型高动态文生视频V1（KJ版）_1979736672185257985.json, 视频生成/文生视频/（4+4步）Wan2.2 Smooth Mix V2高动态差异模型文生视频V1（KJ版）_1979737052461830146.json, 视频生成/文生视频/（6+4步贞贞版）Wan2.2 Smooth Mix V2高动态差异模型文生视频V1（KJ版）_1979737045063077889.json, 视频生成/文生视频/（灰度本地N版）Wan2.2 Smooth Mix V2高低噪模型高动态文生视频V1（KJ版）_1979878092309172225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_105

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/文生视频/1951636109178646529.json、视频生成/文生视频/1960686158676189186.json、视频生成/文生视频/1974801904645574658.json、视频生成/文生视频/1978813759940628482.json、视频生成/文生视频/1978818783190093825.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 15 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
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
- `INTConstant` —— 14/15 个有
- `VHS_VideoCombine` —— 14/15 个有
- `WanVideoTorchCompileSettings` —— 14/15 个有
- `CR Prompt Text` —— 13/15 个有
- `GetImageSizeAndCount` —— 13/15 个有
- `JWInteger` —— 13/15 个有
- `ImageFromBatch+` —— 10/15 个有
- `SaveImage` —— 3/15 个有
- `TT_img_enc` —— 3/15 个有
- `easy seed` —— 2/15 个有
- `LoadImage` —— 1/15 个有
- `MuyeTextEditOutput` —— 1/15 个有
- `SimpleMath+` —— 1/15 个有
- `TT_img_enc_v2` —— 1/15 个有
- `WanVideoContextOptions` —— 1/15 个有
- `WanVideoEasyCache` —— 1/15 个有
- `easy positive` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：SimpleMath+、easy positive、easy seed、ImageFromBatch+、CR Prompt Text
