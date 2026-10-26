---
name: unknown_workflow_video_lora_sampler_439
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.894833
common_nodes: [CreateCFGScheduleFloatList, INTConstant, ImageFromBatch+, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/wan2.2 文生视频_1956285811346079746.json, 视频生成/文生视频/（4+4步）Wan2.2 Smooth Mix V2高低噪模型高动态文生视频V1（KJ版）_1979736672185257985.json, 视频生成/文生视频/（4+4步）Wan2.2 Smooth Mix V2高动态差异模型文生视频V1（KJ版）_1979737052461830146.json, 视频生成/文生视频/（6+4步最佳质量）Wan2.2 Smooth Mix高动态差异模型文生视频V1（KJ版）_1978813759940628482.json, 视频生成/文生视频/（6+4步贞贞版）Wan2.2 Smooth Mix V2高动态差异模型文生视频V1（KJ版）_1979737045063077889.json, 视频生成/文生视频/（6+4步）Wan2.2 Smooth Mix V2模型高低噪同模型高动态文生视频V1（KJ版）_1979736664522264578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_439

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/wan2.2 文生视频_1956285811346079746.json、视频生成/文生视频/（4+4步）Wan2.2 Smooth Mix V2高低噪模型高动态文生视频V1（KJ版）_1979736672185257985.json、视频生成/文生视频/（4+4步）Wan2.2 Smooth Mix V2高动态差异模型文生视频V1（KJ版）_1979737052461830146.json、视频生成/文生视频/（6+4步最佳质量）Wan2.2 Smooth Mix高动态差异模型文生视频V1（KJ版）_1978813759940628482.json、视频生成/文生视频/（6+4步贞贞版）Wan2.2 Smooth Mix V2高动态差异模型文生视频V1（KJ版）_1979737045063077889.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `ImageFromBatch+`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/6 个有
- `GetImageSizeAndCount` —— 5/6 个有
- `JWInteger` —— 5/6 个有
- `LayerColor: Brightness & Contrast` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
