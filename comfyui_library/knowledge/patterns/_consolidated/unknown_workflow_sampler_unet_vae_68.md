---
name: unknown_workflow_sampler_unet_vae_68
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.859786
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/H3-PDMD 4步视频_2117511912073285634.json, 平台全量/MiniMax H3 4步 图片+视频参考 Ref2VA_2092206167903789058.json, 平台全量/MiniMax H3 动作迁移｜原生双参考_2119894663674028034.json, 平台全量/MiniMax H3 短剧工作流｜参考图 + 提示词模板｜提速不减质_2117824295165579266.json, 平台全量/MiniMax H3全能参考（图片、音频、视频皆可参考）_2087510714842963969.json, 平台全量/MiniMax+H3+首尾帧图生视频_2120142782399602689.json, 平台全量/Minimax H3 视频编辑_2084264725461946370.json, 平台全量/minimax_h3_全能参考（参考视频输入）角色替换_2086026217484013569.json, 平台全量/【开源】minimax_h3 视频参考生视频加速版_2085977722513354753.json, 平台全量/【开源】minimax_h3 视频参考生视频加速版_2097203029425606657.json, 数字人/数字人/MiniMax+H3参考生视频6倍加速80GB满配版_2086471377510559745.json, 视频生成/图生视频/MiniMax H3图生视频6倍加速24GB通用版（优化版）_2086460901921742849.json, 视频生成/图生视频/MiniMax H3图生视频6倍加速48GB高配版_2113597089035939841.json, 视频生成/文生视频/BF16 iniMax-H3文生视频、图生视频、多图全能参考、首尾帧+加速版合集全能工作流作流加速版_2084727508074852354.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_68

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/H3-PDMD 4步视频_2117511912073285634.json、平台全量/MiniMax H3 4步 图片+视频参考 Ref2VA_2092206167903789058.json、平台全量/MiniMax H3 动作迁移｜原生双参考_2119894663674028034.json、平台全量/MiniMax H3 短剧工作流｜参考图 + 提示词模板｜提速不减质_2117824295165579266.json、平台全量/MiniMax H3全能参考（图片、音频、视频皆可参考）_2087510714842963969.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 13/14 个有
- `LoadImage` —— 13/14 个有
- `PrimitiveFloat` —— 13/14 个有
- `ResolutionSelector` —— 13/14 个有
- `CreateVideo` —— 11/14 个有
- `SaveVideo` —— 11/14 个有
- `MiniMaxH3ReferenceToVideo` —— 10/14 个有
- `PathchSageAttentionKJ` —— 10/14 个有
- `EasyCache` —— 9/14 个有
- `PrimitiveStringMultiline` —— 9/14 个有
- `VHS_LoadVideo` —— 7/14 个有
- `ImageResizeKJv2` —— 5/14 个有
- `LoraLoaderModelOnly` —— 5/14 个有
- `MiniMaxH3ImageToVideo` —— 5/14 个有
- `VHS_VideoCombine` —— 5/14 个有
- `SolAttnPatch` —— 3/14 个有
- `CR Text` —— 2/14 个有
- `ImageScaleToTotalPixels` —— 2/14 个有
- `MiniMaxH3SigmaShift` —— 2/14 个有
- `Text` —— 2/14 个有
- `孤海注释` —— 2/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `ImageCrop+` —— 1/14 个有
- `LoadAudio` —— 1/14 个有
- `LoadVideoNode` —— 1/14 个有
- `ModelPatchTorchSettings` —— 1/14 个有
- `MuyeTextEditOutput` —— 1/14 个有
- `NotifyPixaroma` —— 1/14 个有
- `UniBlockSwap` —— 1/14 个有
- `忽略多组孤海` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
