---
name: unknown_workflow_sampler_unet_vae
type: Unknown Workflow
frequency: 31
level: moderate
coverage: 0.897613
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimaxH3多参提示词优化_2086425483746566146.json, 视频生成/图生视频/minimaxH3开源版尾帧生视频(8step加速)_2092340433505574914.json, 视频生成/图生视频/minimaxH3开源版尾帧生视频(8step加速)_2096278611857862657.json, 视频生成/图生视频/minimaxH3开源版尾帧生视频_2092343211615412226.json, 视频生成/图生视频/minimaxH3开源版首尾帧(20step)_2092293644232519681.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2092310874190073858.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2092935184156024834.json, 视频生成/图生视频/minimaxH3开源版首尾帧_8step加速__2105856274675093506.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2109460890293727233.json, 视频生成/图生视频/minimaxH3开源版首尾帧(8step加速)_2109652415707443202.json, 视频生成/图生视频/minimaxH3开源版首帧生视频(8step加速)_2092324995224662017.json, 视频生成/图生视频/minimaxH3开源版首帧生视频_2092326575885869057.json, 视频生成/图生视频/minimaxH3把手伸到狗狗面前_2085572965537763330.json, 视频生成/图生视频/minimaxh3-三图参考生视频-15秒动作科幻题材_2097201624564457473.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T10_2085752202936803329.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T1_2085350214604513281.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T2_2085358927612563457.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T3_2085391641258582017.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T4_2085391626901475329.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T5_2085411686395236353.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T6_2085444171992748033.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T7_2102928115411542018.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T7_2104380315761471490.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T8_2085676923673464834.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T9_2085718493915336705.json, 视频生成/图生视频/创意广告_2087007696313733122.json, 视频生成/图生视频/图生视频提示词自动填充_2086756092205428737.json, 视频生成/图生视频/图生视频提示词运镜_2086862647512879105.json, 视频生成/图生视频/图生视频电影质感_2087837157028352001.json, 视频生成/文生视频/MiniMax H3 图生视频（SageAttention 加速版）_2085990371192037378.json, 视频生成/文生视频/Minimax H3 FL2VA 图片首尾帧视频_2095354444597784577.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae

> 由 `engine/knowledge_consolidation` 从 31 个 workflow 归纳得出（视频生成/图生视频/minimaxH3多参提示词优化_2086425483746566146.json、视频生成/图生视频/minimaxH3开源版尾帧生视频(8step加速)_2092340433505574914.json、视频生成/图生视频/minimaxH3开源版尾帧生视频(8step加速)_2096278611857862657.json、视频生成/图生视频/minimaxH3开源版尾帧生视频_2092343211615412226.json、视频生成/图生视频/minimaxH3开源版首尾帧(20step)_2092293644232519681.json…）

- **类型**：Unknown Workflow
- **样本数**：31
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 31 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 25/31 个有
- `Text` —— 19/31 个有
- `PreviewImage` —— 18/31 个有
- `RHHiddenNodes` —— 18/31 个有
- `VHS_VideoCombine` —— 18/31 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 18/31 个有
- `ImageConcatenateMulti_UTK` —— 17/31 个有
- `CreateVideo` —— 14/31 个有
- `SaveVideo` —— 14/31 个有
- `MiniMaxH3ImageToVideo` —— 13/31 个有
- `LoraLoaderModelOnly` —— 11/31 个有
- `LoadAudio` —— 7/31 个有
- `easy showAnything` —— 6/31 个有
- `RH_Translator` —— 2/31 个有
- `easy cleanGpuUsed` —— 1/31 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
