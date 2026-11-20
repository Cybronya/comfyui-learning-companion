---
name: unknown_workflow_video_lora_sampler_456
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.981429
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2动态壁纸生成器_1963239484815028226.json, 视频生成/图生视频/wan2.2 lora_1996855253331058690.json, 视频生成/图生视频/wan2.2图生视频(KJ版)_1951528284905525250.json, 视频生成/图生视频/【动态壁纸】Wan2.2动态壁纸生成器 一键自动循环壁纸MAX版高清_1981177939989499906.json, 视频生成/图生视频/图生视频（人物展示、产品宣传与创意设计）_1979902570766438402.json, 视频生成/图生视频/宠物飞天特效图生视频lora_1955612950611443714.json, 视频生成/图生视频/最新wan2.2图生视频，可在线运行，效果非常OK_1953038544099020801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_456

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan2.2动态壁纸生成器_1963239484815028226.json、视频生成/图生视频/wan2.2 lora_1996855253331058690.json、视频生成/图生视频/wan2.2图生视频(KJ版)_1951528284905525250.json、视频生成/图生视频/【动态壁纸】Wan2.2动态壁纸生成器 一键自动循环壁纸MAX版高清_1981177939989499906.json、视频生成/图生视频/图生视频（人物展示、产品宣传与创意设计）_1979902570766438402.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MathExpression|pysssss` —— 6/7 个有
- `Primitive integer [Crystools]` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `CreateCFGScheduleFloatList` —— 5/7 个有
- `ImageListToImageBatch` —— 4/7 个有
- `ImpactInt` —— 4/7 个有
- `easy imageBatchToImageList` —— 4/7 个有
- `RH_Captioner` —— 3/7 个有
- `Text Multiline` —— 3/7 个有
- `RH_LLMAPI_NODE` —— 2/7 个有
- `GetImageSizeAndCount` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `LoadAudio` —— 1/7 个有
- `RIFE VFI` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
