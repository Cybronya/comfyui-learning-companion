---
name: unknown_workflow_video_sampler_unet_25
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.899769
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3单独放大工作流_2086693326912311298.json, 视频生成/图生视频/H3极速高清文生视频_2089189623070281729.json, 视频生成/图生视频/MINIMAX H3 风扇三段变装展示-双采加速流_2107201355315240961.json, 视频生成/图生视频/MINIMAX-H3 多图参考生视频_2093727758789730305.json, 视频生成/图生视频/MINIMAX-H3 文戏多图参考生视频-手动版_2092909194184839170.json, 视频生成/图生视频/MINIMAX-H3 文戏多图参考生视频_2093644820110725122.json, 视频生成/图生视频/MINIMAX-H3 文戏多图参考生视频_2093665442207457282.json, 视频生成/图生视频/MINIMAX-H3开源 文戏多图参考生视频-手动版_2090385859165122562.json, 视频生成/图生视频/MINIMAX-H3开源 文戏多图参考生视频-手动版_2095839324133744641.json, 视频生成/图生视频/双采样MinimaxH3音频驱动数字人单人版-v1.0_2085408291433304066.json, 视频生成/图生视频/文戏多图参考生视频-MINIMAX-H3 -手动版_2094987834829660161.json, 视频生成/文生视频/MINIMAX-H3 图参考生视频_2091357639291785217.json, 视频生成/文生视频/啊癫 MINIMAX-H3 多参生视频-二采版_2090845897457487873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_25

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/H3单独放大工作流_2086693326912311298.json、视频生成/图生视频/H3极速高清文生视频_2089189623070281729.json、视频生成/图生视频/MINIMAX H3 风扇三段变装展示-双采加速流_2107201355315240961.json、视频生成/图生视频/MINIMAX-H3 多图参考生视频_2093727758789730305.json、视频生成/图生视频/MINIMAX-H3 文戏多图参考生视频-手动版_2092909194184839170.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 12/13 个有
- `LoraLoaderBypassModelOnly` —— 12/13 个有
- `PrimitiveFloat` —— 12/13 个有
- `LoadImage` —— 11/13 个有
- `PT_H3ConcatAVLatent` —— 11/13 个有
- `PrimitiveStringMultiline` —— 11/13 个有
- `VAEEncode` —— 11/13 个有
- `ExtendIntermediateSigmas` —— 10/13 个有
- `H3SigmaRefiner` —— 10/13 个有
- `INTConstant` —— 10/13 个有
- `ImageResizeKJv2` —— 10/13 个有
- `LoadAudio` —— 10/13 个有
- `MiniMaxH3AVDecodeT8` —— 10/13 个有
- `MiniMaxH3ReferenceToVideo` —— 10/13 个有
- `VAEDecode` —— 10/13 个有
- `VAEDecodeAudio` —— 9/13 个有
- `VAEEncodeAudio` —— 9/13 个有
- `MiniMaxH3AudioConditioningT8` —— 2/13 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/13 个有
- `孤海注释` —— 2/13 个有
- `AudioCrop` —— 1/13 个有
- `CLIPTextEncode` —— 1/13 个有
- `CR Text` —— 1/13 个有
- `GetNode` —— 1/13 个有
- `ModelAttentionBackend` —— 1/13 个有
- `PreviewAudio` —— 1/13 个有
- `SetNode` —— 1/13 个有
- `SoundFlow_GetLength` —— 1/13 个有
- `VHS_LoadVideo` —— 1/13 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/13 个有
- `easy clearCacheAll` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
