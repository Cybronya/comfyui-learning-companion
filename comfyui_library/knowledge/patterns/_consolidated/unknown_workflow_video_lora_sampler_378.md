---
name: unknown_workflow_video_lora_sampler_378
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.919143
common_nodes: [CreateCFGScheduleFloatList, INTConstant, JWInteger, SaveImage, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2 Dyno+Remix 1.0新模型超强动态文生视频（KJ版）_1975847976218308609.json, 视频生成/文生视频/Wan2.2 Dyno+Remix文生视频（KJ版）_1974792625356148738.json, 视频生成/文生视频/（灰度本地N版）Wan2.2 Smooth Mix V2高低噪模型高动态文生视频V1（KJ版）_1979878092309172225.json, 视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（KJ版）_1975846186269675522.json, 视频生成/文生视频/（自用）Dyno+Remix文生视频（KJ版）_1974785669753081858.json, 视频生成/文生视频/（自用）KJ版节点套件视频Latent 示范工作流V1_2007518843018678273.json, 视频生成/文生视频/（自用）Wan2.2 文生视频加速版V3（进一步提升速度）_1952589120671559682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_378

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 Dyno+Remix 1.0新模型超强动态文生视频（KJ版）_1975847976218308609.json、视频生成/文生视频/Wan2.2 Dyno+Remix文生视频（KJ版）_1974792625356148738.json、视频生成/文生视频/（灰度本地N版）Wan2.2 Smooth Mix V2高低噪模型高动态文生视频V1（KJ版）_1979878092309172225.json、视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（KJ版）_1975846186269675522.json、视频生成/文生视频/（自用）Dyno+Remix文生视频（KJ版）_1974785669753081858.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `JWInteger`
- `SaveImage`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 6/7 个有
- `TT_img_enc` —— 5/7 个有
- `WanVideoLoraSelect` —— 5/7 个有
- `WanVideoTorchCompileSettings` —— 5/7 个有
- `FastUnsharpSharpen` —— 4/7 个有
- `LoadImage` —— 4/7 个有
- `PrimitiveFloat` —— 4/7 个有
- `Seed (rgthree)` —— 4/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `WanVideoTextEncodeCached` —— 4/7 个有
- `LoadWanVideoT5TextEncoder` —— 3/7 个有
- `WanVideoTextEncode` —— 3/7 个有
- `GetImageSizeAndCount` —— 2/7 个有
- `SaveLatent` —— 2/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `LoadLatent` —— 1/7 个有
- `TT_img_enc_v2` —— 1/7 个有
- `VAEDecode` —— 1/7 个有
- `VAEEncode` —— 1/7 个有
- `VAELoader` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
