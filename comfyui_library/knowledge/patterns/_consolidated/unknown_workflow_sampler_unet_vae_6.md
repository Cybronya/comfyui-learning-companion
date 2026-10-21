---
name: unknown_workflow_sampler_unet_vae_6
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.826609
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 图生视频 最新8步增速工作流+全节点注释_2093916282159714305.json, 视频生成/图生视频/Minimax H3 多参考图生视频 --8步增速工作流_2089535708678676482.json, 视频生成/图生视频/Minimax H3 最新最快4步和8步增速工作流【AI小王子】_2088069368268804097.json, 视频生成/图生视频/Minimax H3 首尾帧生视频   最新8步增速工作流_2088890526631284737.json, 视频生成/图生视频/Minimax H3图生视频--最新8步增速工作流_2088185779976753153.json, 视频生成/图生视频/MinimaxH3开源版参考生视频(8step加速版)_2092363444539453442.json, 视频生成/图生视频/MinimaxH3开源版参考生视频(8step加速版)_2092936286209396737.json, 视频生成/图生视频/MinimaxH3开源版参考生视频(8step加速版)_2094336398261309442.json, 视频生成/图生视频/MinimaxH3开源版参考生视频(8step加速版)_2109218798602641409.json, 视频生成/图生视频/MinimaxH3开源版参考生视频_2092356546490626049.json, 视频生成/图生视频/Minimax参考生视频-(8步加速-768P)_2085357536189960194.json, 视频生成/图生视频/lightx2v 300%加速 MinimaxH3-多参生视频（图片 视频 声音）_2084269573662142465.json, 视频生成/图生视频/【开源】minimax_h3 音频参考生MV_2084184318896857090.json, 视频生成/图生视频/参考生视频_MiniMax H3_2084453784557809665.json, 视频生成/图生视频/参考生视频minimax_h3官方版_2084268345586704386.json, 视频生成/图生视频/开源短剧+电商+游戏视频 Minimax H3 全系列工作流_2089009141858787330.json, 视频生成/图生视频/短剧tvc+电商Minimax H3 最新最快4步和8步增速工作流_2088532906942754817.json, 视频生成/文生视频/MiniMax H3多合一｜Turbo4 + Sage + T8 Stable 组合加速版｜B站UP主@好奇漫步_2086728037277720578.json, 视频生成/文生视频/MiniMax H3多合一｜Turbo4 + Sage + T8 Stable｜R2V Turbo6 EXP + 二采增强版｜B站UP主@好奇漫步_2086836147753410562.json, 视频生成/文生视频/MiniMax H3多合一｜V6_LightX2V官方Turbo4加速版｜B站UP主@好奇漫步_2086676399020142594.json, 视频生成/文生视频/MiniMax_H3三合一_V2｜ComfyUI0.33_Core｜10Eros+LightX2V__2088301741266788353.json, 视频生成/文生视频/MiniMax_H3三合一_V2｜ComfyUI0.33_Core｜LightX2V_v1_4Ste_2088301834657157121.json, 视频生成/文生视频/【0813】MiniMax H3文 图 参考生视频三合一｜组合加速｜全模式二采增强版 B站@好奇漫步_2087029485995642882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 图生视频 最新8步增速工作流+全节点注释_2093916282159714305.json、视频生成/图生视频/Minimax H3 多参考图生视频 --8步增速工作流_2089535708678676482.json、视频生成/图生视频/Minimax H3 最新最快4步和8步增速工作流【AI小王子】_2088069368268804097.json、视频生成/图生视频/Minimax H3 首尾帧生视频   最新8步增速工作流_2088890526631284737.json、视频生成/图生视频/Minimax H3图生视频--最新8步增速工作流_2088185779976753153.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
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
- `MiniMaxH3ReferenceToVideo` —— 20/23 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 19/23 个有
- `BasicScheduler` —— 17/23 个有
- `KSamplerSelect` —— 17/23 个有
- `LoadAudio` —— 17/23 个有
- `GetVideoComponents` —— 15/23 个有
- `LoadVideo` —— 15/23 个有
- `LoraLoaderBypassModelOnly` —— 13/23 个有
- `MiniMaxH3ImageToVideo` —— 12/23 个有
- `LoraLoaderModelOnly` —— 11/23 个有
- `PrimitiveStringMultiline` —— 11/23 个有
- `MiniMaxH3DualClockSamplerT8` —— 10/23 个有
- `CR Prompt Text` —— 6/23 个有
- `ComfySwitchNode` —— 6/23 个有
- `PrimitiveInt` —— 6/23 个有
- `ImageResizeKJv2` —— 5/23 个有
- `CR Float To Integer` —— 4/23 个有
- `PT_H3ConcatAVLatent` —— 4/23 个有
- `VAEEncode` —— 4/23 个有
- `VAEEncodeAudio` —— 4/23 个有
- `VHS_LoadVideo` —— 3/23 个有
- `CR Text` —— 2/23 个有
- `Get Date Time String (JPS)` —— 2/23 个有
- `MiniMaxH3SigmaShift` —— 2/23 个有
- `SaveText|pysssss` —— 2/23 个有
- `ShowText|pysssss` —— 2/23 个有
- `StringFunction|pysssss` —— 2/23 个有
- `WidgetToString` —— 2/23 个有
- `Fast Groups Bypasser (rgthree)` —— 1/23 个有
- `TrimAudioDuration` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
