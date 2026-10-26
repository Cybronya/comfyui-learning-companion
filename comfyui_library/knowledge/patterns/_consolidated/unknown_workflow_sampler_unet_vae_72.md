---
name: unknown_workflow_sampler_unet_vae_72
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.83175
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/mini_max文生视频_2084531376707166209.json, 视频生成/文生视频/minimaxH3开源版文生视频(20step)_2092291766404870146.json, 视频生成/文生视频/minimaxH3开源版文生视频(8step加速)_2090102856362840065.json, 视频生成/文生视频/minimaxH3文生视频工作流（超级加速版V2）_2093311593462456321.json, 视频生成/文生视频/minimaxH3文生视频工作流（超级加速版）_2084925338584436737.json, 视频生成/文生视频/minimax_h3_t2v文生视频_2084177287007784961.json, 视频生成/文生视频/minimax_h3_文生视频4步加速_2084135777386192898.json, 视频生成/文生视频/video_minimax_h3_t2v_2084126777605181442.json, 视频生成/文生视频/video_minimax_h3_t2v_2084826081865068545.json, 视频生成/文生视频/加速版！Minimax H3！开源免费版！文生视频！_2085198371240898561.json, 视频生成/文生视频/智能版minimax+H3+开源版+文生视频+T2VA文生_2084150373744472066.json, 视频生成/文生视频/海螺H3 文生视频-提示词自动优化扩写_2086430630488924162.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_72

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/mini_max文生视频_2084531376707166209.json、视频生成/文生视频/minimaxH3开源版文生视频(20step)_2092291766404870146.json、视频生成/文生视频/minimaxH3开源版文生视频(8step加速)_2090102856362840065.json、视频生成/文生视频/minimaxH3文生视频工作流（超级加速版V2）_2093311593462456321.json、视频生成/文生视频/minimaxH3文生视频工作流（超级加速版）_2084925338584436737.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 12 个 workflow 都包含：
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
- `CreateVideo` —— 10/12 个有
- `SaveVideo` —— 10/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/12 个有
- `PathchSageAttentionKJ` —— 5/12 个有
- `CR Text` —— 4/12 个有
- `LoraLoaderModelOnly` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `EasyCache` —— 2/12 个有
- `Label (rgthree)` —— 2/12 个有
- `MiniMaxH3BlockCacheT8` —— 2/12 个有
- `VHS_VideoCombine` —— 2/12 个有
- `ModelPatchTorchSettings` —— 1/12 个有
- `PainterVRAM` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `RHLLMChatNode` —— 1/12 个有
- `RH_LLMAPI_Pro_Node` —— 1/12 个有
- `SetReserveVRAM` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
