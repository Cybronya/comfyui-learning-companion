---
name: unknown_workflow_sampler_unet_vae_3
type: Unknown Workflow
frequency: 28
level: moderate
coverage: 0.783071
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3多条件参考视频工作流低显存加速版 开源 Ref2VA_2084437517675352065.json, 视频生成/图生视频/MiniMax+H3+参考图图生视频工作流_2084234953285525505.json, 视频生成/图生视频/MiniMax+H3参考生视频_2084466111193636865.json, 视频生成/图生视频/MiniMax-H3   数字人说放唱歌跳舞_2084483238164262914.json, 视频生成/图生视频/MiniMax-H3   数字人说话唱歌跳舞_2084848840682856449.json, 视频生成/图生视频/MiniMax-H3 Ref2va 参考生视频标准版_2095421074551951361.json, 视频生成/图生视频/MiniMax-H3 图生视频 数字人说放唱歌跳舞_2084469631183577089.json, 视频生成/图生视频/MiniMax-H3 多模态参考生视频_2084140670419300353.json, 视频生成/图生视频/MiniMax-H3 多模态参考生视频_2084157109444366337.json, 视频生成/图生视频/MiniMax-H3 数字人说话唱歌跳舞_2084926291026993154.json, 视频生成/图生视频/MiniMax-H3-多图参考视频生成_2084247428697518082.json, 视频生成/图生视频/MiniMax-H3开源版 图片开口说话数字人 图像音频参考生视频_2084239385167482882.json, 视频生成/图生视频/MiniMax-H3开源版 图片开口说话数字人 图像音频参考生视频_2084246078630748161.json, 视频生成/图生视频/MiniMax-H3开源版 声音克隆数字人+全节点注释_2084492386390077442.json, 视频生成/图生视频/MiniMax-H3开源版 数字人（视频+文案）+全节点注释_2084488671373381634.json, 视频生成/图生视频/MiniMax-H3开源版 数字人（视频+文案）+全节点注释_2093665300192514049.json, 视频生成/图生视频/MiniMax-H3数字人（图片+音频）+全节点注释_2084487098446475265.json, 视频生成/图生视频/MiniMax-H3最强开源版 图片开口说话数字人 图像音频参考生视频_2084591926610849793.json, 视频生成/图生视频/MiniMax-H3最强开源版 图片开口说话数字人 图像音频参考生视频_2084625798031568897.json, 视频生成/图生视频/MiniMaxH3 图片数字人！加速版！B站艾橘溪_2084158052382625793.json, 视频生成/图生视频/MiniMaxH3_参考生视频量化加速版_文本_图像_音频_视频_2100207410085457921.json, 视频生成/图生视频/MiniMaxH3_参考生视频量化加速版_文本_图像_音频_视频_2101876284900073474.json, 视频生成/图生视频/The digital avatar speaks H3数字人说话_2100389571778404353.json, 视频生成/图生视频/图生成视频 MiniMax-H3  数字人说放唱歌跳舞_2089165953765560322.json, 视频生成/图生视频/海螺MiniMax-H3开源版 图片开口说话数字人 图像音频参考生视频_2086786651887587329.json, 视频生成/图生视频/海螺h3 MiniMax-H3开源版 图片开口说话数字人 图像音频参考生视频_2084260160511504385.json, 视频生成/文生视频/Minimax+H3+Multi-parameter+Reference+Raw+Video_2084191041938345986.json, 视频生成/文生视频/Minimax_h3官方多参视频生成工作流_2084688064726781954.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多条件参考视频工作流低显存加速版 开源 Ref2VA_2084437517675352065.json、视频生成/图生视频/MiniMax+H3+参考图图生视频工作流_2084234953285525505.json、视频生成/图生视频/MiniMax+H3参考生视频_2084466111193636865.json、视频生成/图生视频/MiniMax-H3   数字人说放唱歌跳舞_2084483238164262914.json、视频生成/图生视频/MiniMax-H3   数字人说话唱歌跳舞_2084848840682856449.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 28 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ReferenceToVideo`
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
- `LoadImage` —— 26/28 个有
- `LoadAudio` —— 23/28 个有
- `PrimitiveStringMultiline` —— 22/28 个有
- `AudioCrop` —— 18/28 个有
- `AILab_QwenVL` —— 13/28 个有
- `JoinStrings` —— 13/28 个有
- `VHS_LoadVideo` —— 11/28 个有
- `PathchSageAttentionKJ` —— 6/28 个有
- `CR Text` —— 4/28 个有
- `EmptyImage` —— 2/28 个有
- `Label (rgthree)` —— 2/28 个有
- `LoadVideo` —— 2/28 个有
- `PreviewImage` —— 2/28 个有
- `CR Prompt Text` —— 1/28 个有
- `CS-MultiImageLoader` —— 1/28 个有
- `PreviewAudio` —— 1/28 个有
- `VHS_LoadAudioUpload` —— 1/28 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
