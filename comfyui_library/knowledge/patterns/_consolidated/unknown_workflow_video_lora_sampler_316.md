---
name: unknown_workflow_video_lora_sampler_316
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.972
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoraLoaderModelOnly, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/chongwuship_2121114339745820674.json, 平台全量/h3-1pass-9img_2117137894283505665.json, 平台全量/能文能武MinimaxH3工作流_2118523834507812865.json, 平台全量/能文能武MinimaxH3工作流_2118874442322497537.json, 平台全量/能文能武MinimaxH3工作流_2118962154979282946.json, 平台全量/能文能武MinimaxH3工作流_2119205922450006018.json, 视频生成/图生视频/MinimaxH3自定义sigam工作流_2109984744522993665.json, 视频生成/图生视频/商业级360度环绕镜头展示工作流_2110737948009385985.json, 视频生成/图生视频/商业级360度环绕镜头展示工作流_2111237385672544258.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_316

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/chongwuship_2121114339745820674.json、平台全量/h3-1pass-9img_2117137894283505665.json、平台全量/能文能武MinimaxH3工作流_2118523834507812865.json、平台全量/能文能武MinimaxH3工作流_2118874442322497537.json、平台全量/能文能武MinimaxH3工作流_2118962154979282946.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxChunkFeedForward` —— 8/9 个有
- `MiniMaxH3Unified` —— 8/9 个有
- `MiniMaxLowVRAMAttention` —— 8/9 个有
- `ModelPreviewOverrideKJ` —— 8/9 个有
- `ResolutionSelector` —— 8/9 个有
- `CR Text` —— 7/9 个有
- `Label (rgthree)` —— 7/9 个有
- `MemoryCleaner` —— 7/9 个有
- `MiniMaxH3SigmaShift` —— 6/9 个有
- `LoadAudio` —— 2/9 个有
- `LoadImage` —— 2/9 个有
- `SetNode` —— 2/9 个有
- `BlockSparseAttention` —— 1/9 个有
- `CM_IntToFloat` —— 1/9 个有
- `FusionText` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `ManualSigmas` —— 1/9 个有
- `MiniMaxH3ReferenceToVideo` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
