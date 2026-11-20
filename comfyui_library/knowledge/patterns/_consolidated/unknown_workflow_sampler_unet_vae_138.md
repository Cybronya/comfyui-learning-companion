---
name: unknown_workflow_sampler_unet_vae_138
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.816333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/MiniMax H3视频编辑_2084240075201794050.json, 平台全量/MiniMax_H3_角色替换_V1.5_Clean_Ref2VA_2114208519141548034.json, 平台全量/Minimax H3 多参考生视频 V20260928_2117444516025290753.json, 平台全量/MinimaxH3视频人物替换_2097258630319009793.json, 平台全量/MinimaxH3视频人物精准替换_2089910908809207809.json, 平台全量/动作迁移Minimax H3 最强视频参考，人物替换_2093803917221122050.json, 视频生成/图生视频/MinimaxH3视频人物替换_2095672328909836290.json, 视频生成/图生视频/MinimaxH3视频人物替换_2109569066229919746.json, 视频生成/图生视频/雷霆运镜Minimax H3 最强视频参考，动作迁移，人物替换_2090101579029504002.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_138

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/MiniMax H3视频编辑_2084240075201794050.json、平台全量/MiniMax_H3_角色替换_V1.5_Clean_Ref2VA_2114208519141548034.json、平台全量/Minimax H3 多参考生视频 V20260928_2117444516025290753.json、平台全量/MinimaxH3视频人物替换_2097258630319009793.json、平台全量/MinimaxH3视频人物精准替换_2089910908809207809.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/9 个有
- `PrimitiveFloat` —— 8/9 个有
- `VHS_LoadVideo` —— 8/9 个有
- `VHS_VideoCombine` —— 8/9 个有
- `CreateVideo` —— 7/9 个有
- `PrimitiveInt` —— 7/9 个有
- `SaveVideo` —— 7/9 个有
- `VAEDecodeAudio` —— 7/9 个有
- `GetImageSize` —— 6/9 个有
- `ImageConcanate` —— 6/9 个有
- `ImageResizeKJv2` —— 6/9 个有
- `PathchSageAttentionKJ` —— 6/9 个有
- `SimpleMath+` —— 6/9 个有
- `VHS_VideoInfo` —— 6/9 个有
- `LoraLoaderModelOnly` —— 2/9 个有
- `MiniMaxH3SigmaShift` —— 2/9 个有
- `ResolutionSelector` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `ModelPreviewOverrideKJ` —— 1/9 个有
- `easy float` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
