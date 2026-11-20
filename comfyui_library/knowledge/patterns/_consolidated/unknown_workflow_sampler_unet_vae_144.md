---
name: unknown_workflow_sampler_unet_vae_144
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.837778
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/mini_max文生视频_2084531376707166209.json, 视频生成/文生视频/minimaxH3开源版文生视频(20step)_2092291766404870146.json, 视频生成/文生视频/minimaxH3开源版文生视频(8step加速)_2090102856362840065.json, 视频生成/文生视频/minimaxH3文生视频工作流（超级加速版V2）_2093311593462456321.json, 视频生成/文生视频/minimaxH3文生视频工作流（超级加速版）_2084925338584436737.json, 视频生成/文生视频/video_minimax_h3_t2v_2084126777605181442.json, 视频生成/文生视频/一键工作流_2088139639545749506.json, 视频生成/文生视频/海螺H3-4步lora工作流_2085326968886743042.json, 视频生成/文生视频/首尾帧加速图minimax_h3_lightx2v生文生ENG_2087087697318998017.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_144

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/mini_max文生视频_2084531376707166209.json、视频生成/文生视频/minimaxH3开源版文生视频(20step)_2092291766404870146.json、视频生成/文生视频/minimaxH3开源版文生视频(8step加速)_2090102856362840065.json、视频生成/文生视频/minimaxH3文生视频工作流（超级加速版V2）_2093311593462456321.json、视频生成/文生视频/minimaxH3文生视频工作流（超级加速版）_2084925338584436737.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 8/9 个有
- `SaveVideo` —— 8/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/9 个有
- `CR Text` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `PathchSageAttentionKJ` —— 3/9 个有
- `Label (rgthree)` —— 2/9 个有
- `LoadImage` —— 2/9 个有
- `CLIPTextEncode` —— 1/9 个有
- `EasyCache` —— 1/9 个有
- `ModelPatchTorchSettings` —— 1/9 个有
- `SetReserveVRAM` —— 1/9 个有
- `VHS_VideoCombine` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
