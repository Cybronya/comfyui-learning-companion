---
name: unknown_workflow_sampler_unet_vae_50
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.850429
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax 4步极速版无缝循环动态壁纸_2085615593344036866.json, 视频生成/图生视频/MiniMax H3 ComfyUI单图参考模板工作流（官方模板）_2084663488521265154.json, 视频生成/图生视频/MiniMax H3 FL2VA-图生视频-优化版_2088003246421004290.json, 视频生成/图生视频/MiniMax H3 FL2VA-图生视频-优化版_2088050578806099969.json, 视频生成/图生视频/MiniMax H3 FL2VA-图生视频-美杜莎_2088070116331311105.json, 视频生成/图生视频/MiniMax H3 I2V-f comfyorg_2085033775163076609.json, 视频生成/图生视频/MiniMax H3 I2V-f-l comfyorg_2086105138632155137.json, 视频生成/图生视频/MiniMax H3 图生视频 加速版工作流_2084933797195370498.json, 视频生成/图生视频/MiniMax H3 无缝循环动态壁纸二次元风格live2d自动分辨率_2085541606505140226.json, 视频生成/图生视频/MiniMax H3 首尾帧 加速版 视频生成工作流_2084941106655096834.json, 视频生成/图生视频/MiniMax H3 首尾帧生视频_2084510292645601281.json, 视频生成/图生视频/MiniMax H3（加速版）｜首尾帧-图文一键生视频_2095787461938073601.json, 视频生成/文生视频/MiniMax H3｜加速版- 图文极速生视频 (15秒视频不到20分钟)_2084980222239272961.json, 视频生成/文生视频/加速版-MiniMax H3｜图文一键生视频_2084935567606894593.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_50

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/MiniMax 4步极速版无缝循环动态壁纸_2085615593344036866.json、视频生成/图生视频/MiniMax H3 ComfyUI单图参考模板工作流（官方模板）_2084663488521265154.json、视频生成/图生视频/MiniMax H3 FL2VA-图生视频-优化版_2088003246421004290.json、视频生成/图生视频/MiniMax H3 FL2VA-图生视频-优化版_2088050578806099969.json、视频生成/图生视频/MiniMax H3 FL2VA-图生视频-美杜莎_2088070116331311105.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 12/14 个有
- `VAEDecodeAudio` —— 12/14 个有
- `GetImageSize` —— 11/14 个有
- `ImageScaleToTotalPixels` —— 11/14 个有
- `PathchSageAttentionKJ` —— 6/14 个有
- `EasyCache` —— 4/14 个有
- `CR Prompt Text` —— 3/14 个有
- `DF_Int_to_Float` —— 3/14 个有
- `MiniMaxH3SigmaShift` —— 3/14 个有
- `ShowAnything|Mie` —— 3/14 个有
- `GetNode` —— 2/14 个有
- `ImageFromBatch` —— 2/14 个有
- `ImpactSwitch` —— 2/14 个有
- `LoraLoaderModelOnly` —— 2/14 个有
- `SetNode` —— 2/14 个有
- `LoraLoaderBypassModelOnly` —— 1/14 个有
- `ResizeAndPadImage` —— 1/14 个有
- `ResizeImageMaskNode` —— 1/14 个有
- `TextInputNode` —— 1/14 个有
- `easy imageScaleDownToSize` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
