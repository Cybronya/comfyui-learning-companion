---
name: unknown_workflow_lora_sampler_unet_41
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.797
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ComfySwitchNode, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/桌面女友_2110568224566890498.json, 视频生成/图生视频/桌面女友_2111091294834614273.json, 视频生成/图生视频/（首尾帧 2图）MINIMAX H3  图生视频_2111267377957658625.json, 视频生成/文生视频/全模態影音生成，畫面與聲音一次算出來；支援首尾幀控制、內建 8 步 Turbo 開關_2100568061072994305.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_41

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/桌面女友_2110568224566890498.json、视频生成/图生视频/桌面女友_2111091294834614273.json、视频生成/图生视频/（首尾帧 2图）MINIMAX H3  图生视频_2111267377957658625.json、视频生成/文生视频/全模態影音生成，畫面與聲音一次算出來；支援首尾幀控制、內建 8 步 Turbo 開關_2100568061072994305.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `ImageCompositeMasked` —— 2/4 个有
- `ImageScale` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `Int` —— 2/4 个有
- `ManualSigmas` —— 2/4 个有
- `QwenImage21Cache` —— 2/4 个有
- `SamplerCustom` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `TextEncodeQwenImage21` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `Wan_Organic_Skin` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
