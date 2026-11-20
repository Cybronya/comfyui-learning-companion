---
name: unknown_workflow_video_lora_sampler_312
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.742889
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, CR Text Concatenate, CR Text Replace, Int, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewAny, RHLLMChatNode, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/MMH3 上半身展示_2089191677608153090.json, 平台全量/MMH3 全身展示-角色模型资产库_动漫人物角色lora训练集_3D动漫资产_2087699927005745153.json, 平台全量/MMH3 往前行走展示_2093867189723029506.json, 视频生成/图生视频/MiniMaxH3 双人 完美数字人_2089941203092590593.json, 视频生成/图生视频/MiniMaxH3 双人 完美数字人_2092253052395941889.json, 视频生成/图生视频/MiniMaxH3 双人 完美数字人_2092436981681844226.json, 视频生成/图生视频/MiniMaxH3 完美数字人_2086312040032989186.json, 视频生成/图生视频/MiniMaxH3 数字人走路说话 维吾尔族语_2089970449554956290.json, 视频生成/文生视频/开源版MinimaxH3完美口播带货数字人参考音频数字人短视频带货_2086540418640076801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_312

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/MMH3 上半身展示_2089191677608153090.json、平台全量/MMH3 全身展示-角色模型资产库_动漫人物角色lora训练集_3D动漫资产_2087699927005745153.json、平台全量/MMH3 往前行走展示_2093867189723029506.json、视频生成/图生视频/MiniMaxH3 双人 完美数字人_2089941203092590593.json、视频生成/图生视频/MiniMaxH3 双人 完美数字人_2092253052395941889.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Replace`
- `Int`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewAny`
- `RHLLMChatNode`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 6/9 个有
- `StringToInt` —— 6/9 个有
- `VAEDecodeAudio` —— 6/9 个有
- `ttN concat` —— 6/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `ImageBatchMultiV2` —— 3/9 个有
- `IntToString` —— 3/9 个有
- `JWFloat` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `floatToInt _O` —— 3/9 个有
- `llama_cpp_instruct_adv` —— 3/9 个有
- `llama_cpp_model_loader` —— 3/9 个有
- `llama_cpp_parameters` —— 3/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
