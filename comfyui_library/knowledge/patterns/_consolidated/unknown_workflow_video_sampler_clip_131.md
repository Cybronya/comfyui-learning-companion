---
name: unknown_workflow_video_sampler_clip_131
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9204
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSamplerSelect, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEEncode, VAEEncodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/视频高清修复  MiniMax H3_2089888954760908802.json, 平台全量/视频高清修复  MiniMax H3_2098243901634211842.json, 平台全量/视频高清修复-MiniMax H3_2089244029333630977.json, 平台全量/👾怪獸-视频高清修复  MiniMax H3👾_2092919268869500929.json, 视频生成/图生视频/H3单独放大工作流_2086693326912311298.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_131

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/视频高清修复  MiniMax H3_2089888954760908802.json、平台全量/视频高清修复  MiniMax H3_2098243901634211842.json、平台全量/视频高清修复-MiniMax H3_2089244029333630977.json、平台全量/👾怪獸-视频高清修复  MiniMax H3👾_2092919268869500929.json、视频生成/图生视频/H3单独放大工作流_2086693326912311298.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PT_H3ConcatAVLatent`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 4/5 个有
- `ImageConcanate` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `Int` —— 3/5 个有
- `PrimitiveBoolean` —— 3/5 个有
- `easy ifElse` —— 3/5 个有
- `孤海注释` —— 3/5 个有
- `CR Text` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
