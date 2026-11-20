---
name: unknown_workflow_sampler_vae_12
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.951565
common_nodes: [CreateVideo, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3Ref2VAEncode, RHMiniMaxH3Ref2VAModelLoader, RHMiniMaxH3Ref2VATarget, RHMiniMaxH3Ref2VATextEncoderLoader, RHMiniMaxH3Ref2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [平台全量/MiniMax H3 Ref2VA开源版（视频+音频）-多图参考生视频_2084622691105075202.json, 平台全量/MiniMax H3开源 视频参考生视频_2088941636821807106.json, 平台全量/MiniMax H3开源 视频参考生视频_2088970019525980161.json, 平台全量/MiniMaxH3【视频参考+图片参考】多模态生视频_2084656712409239554.json, 平台全量/MiniMaxH3视频参考生视频_2084643611563614210.json, 数字人/数字人/MiniMax+H3+FL2VA开源版-多图参考生视频_2084476749886353409.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-图像 音频参考生视频_2084444621870026754.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-图像 音频参考生视频_2085050440319852545.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-图像 音频参考生视频_2087342773396660225.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-多图参考生视频_2087744764446863362.json, 视频生成/图生视频/MiniMax H3 ref2va(图片+音频)开源版-多图参考生视频_2084568199366004738.json, 视频生成/图生视频/MiniMax+H3+FL2VA开源版-图像+音频参考生视频_2110975898894819330.json, 视频生成/图生视频/MiniMaxH3【1参考图+2音频】多模态生视频_2089902638996480002.json, 视频生成/图生视频/MiniMaxH3【2参考图+1音频】多模态生视频_2089938231520481282.json, 视频生成/图生视频/MiniMaxH3【3参考图+1音频】多模态生视频_2089942418257965058.json, 视频生成/图生视频/MiniMaxH3【三参考图+双音频】多模态生视频_2084628840730681346.json, 视频生成/图生视频/MiniMaxH3【三参考图+双音频】多模态生视频_2088428146709327873.json, 视频生成/图生视频/MiniMaxH3【三参考图+双音频】多模态生视频_2095729142108082177.json, 视频生成/图生视频/MiniMaxH3【参考图+音频】多模态生视频_2084556279430868993.json, 视频生成/图生视频/MiniMaxH3【双参考图+双音频】多模态生视频_2084609112222031873.json, 视频生成/图生视频/MiniMaxH3三参考生视频_2084522903437135874.json, 视频生成/图生视频/MiniMaxH3单参考生视频_2084327376875515906.json, 视频生成/图生视频/MiniMaxH3双参考生视频_2084512077250650113.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_12

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（平台全量/MiniMax H3 Ref2VA开源版（视频+音频）-多图参考生视频_2084622691105075202.json、平台全量/MiniMax H3开源 视频参考生视频_2088941636821807106.json、平台全量/MiniMax H3开源 视频参考生视频_2088970019525980161.json、平台全量/MiniMaxH3【视频参考+图片参考】多模态生视频_2084656712409239554.json、平台全量/MiniMaxH3视频参考生视频_2084643611563614210.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 23 个 workflow 都包含：
- `CreateVideo`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3Ref2VAEncode`
- `RHMiniMaxH3Ref2VAModelLoader`
- `RHMiniMaxH3Ref2VATarget`
- `RHMiniMaxH3Ref2VATextEncoderLoader`
- `RHMiniMaxH3Ref2VAVAELoader`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 19/23 个有
- `RHMiniMaxH3Ref2VAImageReference` —— 19/23 个有
- `CR Text` —— 17/23 个有
- `DF_Int_to_Float` —— 15/23 个有
- `Int` —— 15/23 个有
- `LoadAudio` —— 14/23 个有
- `RHMiniMaxH3Ref2VAAudioReference` —— 14/23 个有
- `LoadVideo` —— 5/23 个有
- `RHMiniMaxH3Ref2VAVideoReference` —— 5/23 个有
- `孤海注释` —— 2/23 个有
- `MmuuaiGroupBypass` —— 1/23 个有
- `MuyeTextEditOutput` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
