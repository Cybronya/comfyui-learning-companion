---
name: unknown_workflow_sampler_unet_vae_17
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.604737
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3+人物替换H3+ Character Replacement—Smart Reverse-Eng_2108715812382142465.json, 视频生成/图生视频/MiniMax H3-全能参考  三图版+一视频_2094421879401574401.json, 视频生成/图生视频/MiniMax H3-全能参考-三图版_2094413856083898369.json, 视频生成/图生视频/MiniMax H3-全能参考-双图版_2089995459833192449.json, 视频生成/图生视频/MiniMax H3-全能参考-四图版_2094418452898476034.json, 视频生成/图生视频/MiniMax H3-全能参考一图版_2094433073793421313.json, 视频生成/图生视频/MiniMax H3全能参考生视频_2084114253300199425.json, 视频生成/图生视频/MiniMax H3全能参考生视频（LightX2V加速LORA）_2087383302742298625.json, 视频生成/图生视频/MiniMax H3全能参考生视频（LightX2V加速LORA）（9参考图3视频）_2087443247135281154.json, 视频生成/图生视频/MiniMax H3全能参考生视频（自定义背景+自定义人物+动作迁移）​_2088807649155567617.json, 视频生成/图生视频/MiniMax H3全能参考生视频，图片、视频。音频参考（动作迁移）_2085606340298366977.json, 视频生成/图生视频/MiniMax H3：参考生视频_2095783894242127874.json, 视频生成/图生视频/MiniMax_H3_七套服装连续换装_2094786595428847617.json, 视频生成/图生视频/Minimax H3 人物替换-智能反推提示词_2088896890543894530.json, 视频生成/图生视频/h3自定义背景人物换视频背景人物全能参考 MiniMax H3动作迁移图生视频工作流_2092949782200414209.json, 视频生成/图生视频/h3自定义背景换视频背景人物全能参考 MiniMax H3动作迁移图生视频工作流_2092910196111794178.json, 视频生成/图生视频/自定义背景人物全能参考 MiniMax H3动作迁移图生视频工作流_2091761423037853697.json, 视频生成/文生视频/MiniMax H3全能参考生视频（动作迁移）_2084473001717878785.json, 视频生成/文生视频/MiniMax H3多参2倍速（开源版）V2_2086281240478576641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_17

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/H3+人物替换H3+ Character Replacement—Smart Reverse-Eng_2108715812382142465.json、视频生成/图生视频/MiniMax H3-全能参考  三图版+一视频_2094421879401574401.json、视频生成/图生视频/MiniMax H3-全能参考-三图版_2094413856083898369.json、视频生成/图生视频/MiniMax H3-全能参考-双图版_2089995459833192449.json、视频生成/图生视频/MiniMax H3-全能参考-四图版_2094418452898476034.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 18/19 个有
- `LoraLoaderModelOnly` —— 17/19 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 17/19 个有
- `GetNode` —— 12/19 个有
- `SetNode` —— 12/19 个有
- `VHS_LoadVideo` —— 12/19 个有
- `Fast Groups Bypasser (rgthree)` —— 11/19 个有
- `LoadAudio` —— 10/19 个有
- `CR Prompt Text` —— 9/19 个有
- `PrimitiveInt` —— 9/19 个有
- `PrimitiveStringMultiline` —— 8/19 个有
- `ComfySwitchNode` —— 7/19 个有
- `PrimitiveBoolean` —— 7/19 个有
- `EasyCache` —— 3/19 个有
- `LoadVideo` —— 2/19 个有
- `RHHiddenNodes` —— 2/19 个有
- `easy showAnything` —— 2/19 个有
- `MiniMaxH3BlockCacheT8` —— 1/19 个有
- `MiniMaxH3SigmaShift` —— 1/19 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
