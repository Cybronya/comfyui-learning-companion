---
name: unknown_workflow_sampler_unet_vae_330
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.788
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, ManualSigmas, PreviewAny, PrimitiveInt, PrimitiveStringMultiline, RemakeConditioning, RemakeKeyframeUntil, RemakeNoise, SamplerCustomAdvanced, SaveVideo, StringFormat, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo]
problems: []
missing: []
members: [平台全量/H3-Viggle-Remake视频重制万物替换_2118602184114925570.json, 平台全量/Viggle-Remake-Character-Swap 视频角色替换工作流_2119011334514888705.json, 平台全量/Viggle-Remake视频换人_2118702201924317186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_330

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/H3-Viggle-Remake视频重制万物替换_2118602184114925570.json、平台全量/Viggle-Remake-Character-Swap 视频角色替换工作流_2119011334514888705.json、平台全量/Viggle-Remake视频换人_2118702201924317186.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `ManualSigmas`
- `PreviewAny`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RemakeConditioning`
- `RemakeKeyframeUntil`
- `RemakeNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `StringFormat`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/3 个有
- `DF_Int_to_Float` —— 2/3 个有
- `GetImageRangeFromBatch` —— 2/3 个有
- `LoraLoaderBypassModelOnly` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `QwenH3PromptLocal` —— 2/3 个有
- `TextInput_` —— 2/3 个有
- `CRT_IntToString` —— 1/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `QwenImage21Cache` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `TextEncodeQwenImage21` —— 1/3 个有
- `VRAM_Debug` —— 1/3 个有
- `easy batchAnything` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |
| 采样步数 | 25 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | beta | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
